from tkinter import Entry, END

__author__ = 'xwffirilat'


class Input(Entry):
    MAX_HISTORY = 15

    # noinspection PyDefaultArgument,PyShadowingNames
    def __init__(self, tk, interpreter, output, cnf={}, **kwargs):
        super().__init__(tk, cnf, **kwargs)
        self._defaultCallback = lambda *args, **kwargs: ''
        self.output = output
        self.interpreter = interpreter
        self.promptCallback = self._defaultCallback
        self.history = []
        self.historyPoint = 0
        self.bind('<Return>', self.interpret)
        self.bind('<Up>', self.upHistory)
        self.bind('<Down>', self.downHistory)

    # noinspection PyUnusedLocal
    def interpret(self, event):
        inp = self.get()
        self.history.append(inp)
        self.historyPoint = 0
        if len(self.history) > Input.MAX_HISTORY:
            del self.history[0]
        if self.promptCallback is not self._defaultCallback:
            self.output.add(self.promptCallback(inp))
            self.promptCallback = self._defaultCallback
        else:
            self.output.add(self.interpreter.interpret(inp))
        self.delete(0, END)

    # noinspection PyUnusedLocal
    def upHistory(self, event):
        if self.historyPoint == len(self.history):
            return

        self.historyPoint += 1
        new = self.history[-self.historyPoint]
        self.delete(0, END)
        self.insert(0, new)

    # noinspection PyUnusedLocal
    def downHistory(self, event):
        if self.historyPoint == 0:
            self.delete(0, END)
            return
        self.historyPoint -= 1
        if self.historyPoint == 0:
            self.delete(0, END)
            return
        new = self.history[-self.historyPoint]
        self.delete(0, END)
        self.insert(0, new)

    def setCallback(self, func):
        self.promptCallback = func
