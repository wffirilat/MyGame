from internal.exception import CommandException

__author__ = 'xwffirilat'


def apply(*args, **kwargs):
    def _inner(func):
        return func(*args, **kwargs)

    return _inner


@apply()
class CommandRegistry(dict):
    def __setitem__(self, key: str, value):
        if key not in self.keys():
            super().__setitem__(key, value)
        else:
            raise CommandException('Command "%s" already registered' % key)

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except KeyError:
            raise CommandException('Command not recognized: "%s"' % item)
