__author__ = 'xwffirilat'

import os

for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    __import__('mods.' + module[:-3], locals(), globals())
