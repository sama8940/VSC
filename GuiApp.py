import configparser, os, sys, tkinter, webbrowser
from tkinter import messagebox

class GuiApp:
    def __init__(self, root:tkinter.Tk):
        root.title(self.__class__.__name__)
        self.iniFilename = os.path.abspath(
            __file__).replace('.py', '.ini')
        
        clientX = '200'
        clientY = '200'
        clientHeight = '100'
        cliientWidth = '300'
        cp = configparser.ConfigParser()
        try:
            cp.read(self.iniFilename)
            clientX = cp['Client']['X']
            clientY = cp['Client']['Y']
            clientHeight = cp['Client']['Height']
            cliientWidth = cp['Client']['Width']
        
        except:
            print(self.__class__.__name__ +
                  ': Use defalut value(s)' , file=sys.stderr)
            root.geometry(self.__class__.__name__ +
                  '+' + clientX + '+' + clientY)