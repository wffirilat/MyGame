from internal.exception import GameException

__author__ = 'xwffirilat'


def apply(*args, **kwargs):
    def _inner(func):
        return func(*args, **kwargs)

    return _inner


@apply()
class LocationRegistry(dict):
    def __setitem__(self, key: str, value):
        if key not in self.keys():
            super().__setitem__(key, value)
        else:
            raise GameException('Location "%s" already registered' % key)