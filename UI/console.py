from tkinter import Text, END

__author__ = 'xwffirilat'


class Console(Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._indent = []

    def add(self, line):
        if line != '':
            self.insert(END, (''.join(self._indent)) + line + '\n')
        self.see(END)

    def delete(self, index1, index2=None):
        pass

    def indent(self, tag):
        self._indent . append(tag)

    def dedent(self):
        del self._indent[-1]
