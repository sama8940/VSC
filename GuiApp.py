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
        root.geometry(cliientWidth  + 'x'  + clientHeight +'+' + clientX + '+' + clientY)
        root.option_add(' *tearOff' , tkinter.FALSE)
        menu = tkinter.Menu()
        menuFile = tkinter.Menu()
        menu.add_cascade(menu=menuFile, label= 'ファイル(F)', underline=5)
        menuFile.add_command(label='終了(X)', underline=3,
            command=self.menuFileExit, accelerator='ALT+F4')
        menuHelp = tkinter.Menu()
        menu.add_cascade(menu=menuHelp, label='ヘルプ(H)', underline=4)
        menuHelp.add_command(label='ヘルプファイルを開く(O)',
            underline=10, command=self.menuHelpOpenWeb)
        menuHelp.add_command(label='バージョン情報(V)',
            underline=8, command=self.menuHelpVersion)
        root['menu'] = menu
        #root.bind_all('<Alt-F4>', self.menuFileExit)
        root.protocol('WM_DELETE_WINDOW', self.menuFileExit)

    def menuFileExit(self, event=None):
        cp = configparser.ConfigParser()
        cp['Client'] = {
            'X': str(root.winfo_x()),
            'Y': str(root.winfo_y()),
            'Height': str(root.winfo_height()),
            'Width': str(root.winfo_width())
        }
        with open(self.iniFilename, 'w') as f:
            cp.write(f)
        root.destroy()

    def menuHelpOpenWeb(self):
        helpFilePath = os.path.dirname(__file__) + os.sep + 'help.html'
        if os.path.isfile(helpFilePath):
            helpFilePath = 'file:///' + helpFilePath.replace(os.sep, '/')
            webbrowser.open(helpFilePath)
        else:
            messagebox.showerror(self.__class__.__name__,
                helpFilePath    + 'がありません')

    def menuHelpVersion(self):
        s = self.__class__.__name__
        s += ' Verson 0.01(2023/06/01)\n'
        s += '@2023 Hideo Harada\n'
        s += 'with Python ' + sys.version
        messagebox.showinfo(self.__class__.__name__, s)

root = tkinter.Tk()
GuiApp(root)
root.mainloop()