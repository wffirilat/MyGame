from tkinter import Frame, Label, Entry

__author__ = 'xwffirilat'


class LabelEntry(Frame):
    def __init__(self, tk, name, text, **kwargs):
        super().__init__(tk, **kwargs)
        self.label = Label(self, text=name)
        self.entry = Entry(self, text=text)
        self.label.grid(row=0, column=0)
        self.entry.grid(row=0, column=1)

    def updateText(self, text):
        self.entry.configure(text=text)
