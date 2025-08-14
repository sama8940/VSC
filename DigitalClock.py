import datetime, locale, tkinter

class DigitalClock:
    def __init__(self, root:tkinter.Tk):
        root.title(self.__class__.__name__)
        root.geometry('240x60') 
        self.canvas = tkinter.Canvas(root, bg='#FFFFFF')
        self.canvas.pack(expand=True, fill=tkinter.BOTH)
        self.afterId = None
        locale.setlocale(locale.LC_TIME, 'ja_JP')
        root.bind('<Configure>', self.configured)

    def configured(self, event):
        self.update()

    def update(self):
        if self.afterId != None:
            root.after_cancel(self.afterId)
        self.canvas.delete('all')
        self.canvas.create_text(
            self.canvas.winfo_width() // 2,
            self.canvas.winfo_height() // 2,
            text=datetime.datetime.now().strftime(
            '%Y年%m月%d日(%a) %H:%M:%S'))
        self.afterId = root.after(100, self.update)
        
root = tkinter.Tk()
DigitalClock(root)
root.mainloop()
