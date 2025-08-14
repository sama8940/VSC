import tkinter
from tkinter import messagebox

class FirstGui:
    def __init__(self, root:tkinter.Tk):
        root.title(self.__class__.__name__)
        root.geometry('300x100')
        button = tkinter.Button(
            text = '押してください!' ,
            command = self.buttonClicked)
        button.pack()

    def buttonClicked(self):
        messagebox.showinfo(
             self.__class__.__name__,
            'ありがとうございます!')

root = tkinter.Tk()
FirstGui(root)
root.mainloop()