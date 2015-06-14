__author__ = 'wffirilat'
from enum import Enum


class EventType(type):
    """
    Metaclass to add a clean listeners attribute to Event subclasses.
    """

    def __init__(cls, name, parents, dct):
        # Is there a better way to do this?
        cls.listeners = getCleanListenerList()
        super().__init__(name, parents, dct)

    @property
    def hasListeners(cls):
        return any((len(i) != 0 for i in cls.listeners.values()))


def post(event):
    """
    Send the event to all listeners (including superclass listeners)
    in priority order, then specific to general.

    Returns the modified event.

    :type event: Event
    :return: said event after modifications
    """

    # can anyone make this faster?
    typ = type(event)
    typeList = [typ]
    while typeList[-1] != Event:
        typeList.append(typeList[-1].mro()[1])
    for priority in PRIORITY_LIST:
        for typ in typeList:
            if typ.hasListeners:
                for listener in typ.listeners[priority]:
                    if not event.canceled or listener.recieveCanceled:
                        event = listener(event)
    return event


def decorator(deco):
    """
    helper function to make decorators preserve docstrings, ect.
    """

    def new(f):
        g = deco(f)
        g.__name__ = f.__name__
        g.__doc__ = f.__doc__
        g.__dict__.update(f.__dict__)
        return g

    new.__name__ = decorator.__name__
    new.__doc__ = decorator.__doc__
    new.__dict__.update(decorator.__dict__)
    return new


class Result(Enum):
    """
    Results of events.
    """
    ALLOW = 'ALLOW'
    DEFAULT = 'DEFAULT'
    DENY = 'DENY'


class Priority(Enum):
    """
    Priorities for handler execution ordering.
    """
    LOWEST = 'LOWEST'
    LOW = 'LOW'
    NORMAL = 'NORMAL'
    HIGH = 'HIGH'
    HIGHEST = 'HIGHEST'


PRIORITY_LIST = [Priority.HIGHEST, Priority.HIGH, Priority.NORMAL, Priority.LOW, Priority.LOWEST]


def getCleanListenerList():
    return {Priority.HIGHEST: [],
            Priority.HIGH: [],
            Priority.NORMAL: [],
            Priority.LOW: [],
            Priority.LOWEST: []}


class Event(metaclass=EventType):
    """
    Base class for Events.
    SUBCLASS THIS to make new events.
    Don't forget super().__init__().
    """
    listeners = None
    isCancelable = False
    hasResult = True

    def __init__(self):
        self._canceled = False
        self._result = Result.DEFAULT

    @property
    def canceled(self):
        return self._canceled

    @canceled.setter
    def canceled(self, val):
        if self.__class__.isCancelable:
            self._canceled = val
        elif val:
            raise RuntimeError("Attempted to cancel an un-cancelable event")

    @property
    def result(self):
        return self._canceled

    @result.setter
    def result(self, val):
        if self.__class__.hasResult:
            self._result = val
        else:
            raise RuntimeError(
                "Attempted to assign result to result-less event")

    def cancel(self):
        self.canceled = True


def cancelable(eventClass: EventType):
    """
    Decorator for Event subclasses to allow an event to be canceled.
    USE THIS or canceling events will raise a RuntimeError.
    """
    if issubclass(eventClass, Event):
        eventClass.isCancelable = True
    return eventClass


# is this useful for anything?
def noResult(eventClass: EventType):
    """
    Decorator for Event subclasses to say an event has no Result.
    May not be useful.
    """
    if issubclass(eventClass, Event):
        eventClass.hasResult = False
    return eventClass


class EventHandler:
    def __init__(self, eventType=None, priority=Priority.NORMAL, receiveCanceled=False):
        self.func = lambda event: None
        self.eventType = eventType
        self.priority = priority
        self.receiveCanceled = receiveCanceled
        self.isSetup = False

    def _setup(self, func):
        """sets up EventHandler to call func,
        grabbing handled EventType from annotations if necessary"""
        self.func = func

        if self.eventType is None:
            for ann in self.func.__annotations__:
                # search through annotations for EventType
                # should it be required to name parameter 'event'?
                if type(self.func.__annotations__[ann]) is EventType:
                    self.eventType = self.func.__annotations__[ann]
                    break
            else:
                raise TypeError('You need to specify eventType, either with parameters or annotations.')

        self.eventType.listeners[self.priority].append(self)

        self.isSetup = True

    def __call__(self, event):
        if not self.isSetup:
            # setup self and return
            self._setup(event)
            return self
        else:
            self.func(event)
            # return event automagically
            return event

    def disable(self):

        try:
            self.eventType.listeners[self.priority].remove(self)
        except ValueError:
            pass

    def reenable(self):
        if self not in self.eventType.listeners[self.priority]:
            self.eventType.listeners[self.priority].append(self)
