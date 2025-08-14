import configparser, os, sys, tkinter, webbrowser
from tkinter import messagebox
DELIMITER = '\a' #BEL
if os.name == 'nt':
    FONT = 'Meryo UI'
    WINDOWS_ENCODING = 'cp932'
elif os.name == 'posix':
    FONT = 'Hiragino Sans GB'
INTERVAL = 250

class TextClipper:
    def __init__(self, root):
        root.title(self.__class__.__name__)
        self.iniFilename = os.path.abspath(__file__).replace('.py', '.ini')
        clientX = '200'
        clientY = '200'
        clientHeight = '100'
        clientWidth = '300'
        self.fontsize = 12
        clipboardStrings = ''
        cp = configparser.ConfigParser()
        try:
            cp.read(self.iniFilename)
            clientX = cp['Client']['X']
            clientY = cp['Client']['Y']
            clientHeight = cp['Client']['Height']
            clientWidth = cp['Client']['Width']
            self.fontsize = int(cp['Client']['Size'])
            clipboardStrings = cp['Clipboard']['Strings']
        except:
            print(self.__class__.__name__ + ': Use default value(s)' , file=sys.stderr)
        root.geometry(f'{clientWidth}x{clientHeight}+{clientX}+{clientY}')
        self.listboxMain = tkinter.Listbox(root, selectmode=tkinter.SINGLE, activestyle=tkinter.NONE, font=(FONT, self.fontsize))
        clipboardStringList = clipboardStrings.split(DELIMITER)
        for s in clipboardStringList:
            if s != '':
                self.listboxMain.insert(tkinter.END, s)
        
        root.option_add('*tearOff', tkinter.FALSE)
        menu = tkinter.Menu(root)
        menuFile = tkinter.Menu()
        menu.add_cascade(menu=menuFile, label='ファイル(F)', underline=5)
        menuFile.add_command(label='終了(E)', underline=3, command=self.menuFileExit, accelerator='ALT+F4')
        menuEdit = tkinter.Menu()
        menu.add_cascade(menu=menuEdit, label='編集(E)', underline=3)
        menuEdit.add_command(label='選択項目をクリップボードにコピー(C)', underline=17, command=self.menuEditCopy, accelerator='CTRL+C')  
        menuEdit.add_command(label='全項目をクリップボードにコピー(A)', underline=16, command=self.menuEditCopyALL)
        menuEdit.add_command(label='全項目を並び替えてクリップボードにコピー(S)', underline=21, command=self.menuEditCopyAllSorted)
        menuEdit.add_command(label='選択項目を削除(D)', underline=8, command=self.menuEditDelete, accelerator='Delete')
        menuEdit.add_command(label='全項目を削除(E)', underline=7, command=self.menuEditDeleteAll)
        menuEdit.add_command(label='選択項目をwebブラウザーで開く(O)', underline=17, command=self.menuEditOpenWeb)
        menuSetting = tkinter.Menu()
        menu.add_cascade(menu=menuSetting, label='設定(S)', underline=3)
        menuSetting.add_command(label='文字を大きく(B)', underline=7, command=self.menuSettingFontBigger, accelerator='B')
        menuSetting.add_command(label='文字を小さく(S)', underline=7, command=self.menuSettingFontSmaller, accelerator='S')
        menuHelp = tkinter.Menu()
        menu.add_cascade(menu=menuHelp, label='ヘルプ(H)', underline=4)
        menuHelp.add_command(label='ヘルプファイルを開く(O)', underline=10, command=self.menuHelpOpenWeb)
        menuHelp.add_command(label='ヴァージョン情報(V)', underline=8, command=self.menuHelpVersion)
        root['menu'] = menu
        #root.bind('<ALT-F4>', self.menuFileExit)
        root.protocol('WM_DELETE_WINDOW', self.menuFileExit)

        scrollbarMain = tkinter.Scrollbar(root, orient=tkinter.VERTICAL, command=self.listboxMain.yview)
        self.listboxMain.config(yscrollcommand=scrollbarMain.set)
        scrollbarMain.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
        self.listboxMain.pack(fill=tkinter.BOTH, expand=True)

        self.afterId = None
        self.clipboardContent = ''
        self.currentSelectionWillBeTop = False
        root.bind('<Configure>', self.configured)
        root.bind('<Delete>', self.menuEditDelete)
        root.bind('<b>', self.menuSettingFontBigger)
        root.bind('<s>', self.menuSettingFontSmaller)
    
    def menuFileExit(self):
        cp = configparser.ConfigParser()
        cp['Client'] = {
            'X': str(root.winfo_x()),
            'Y': str(root.winfo_y()),
            'Height': str(root.winfo_height()),
            'Width': str(root.winfo_width()),
        }
        cp['Font'] = {
            'Size': str(self.fontsize)
        }
        clipboardStrings = DELIMITER
        for s in self.listboxMain.get(0, tkinter.END):
            clipboardStrings += s + DELIMITER
        if os.name == 'nt':
            try:
                s = clipboardStrings.encode(WINDOWS_ENCODING)
            except UnicodeEncodeError: 
                messagebox.showwarning(self.__class__.__name__, 'INIファイルに保存できない文字を[?]に置き換えます')
            s = clipboardStrings.encode(WINDOWS_ENCODING, errors = 'replace')
            clipboardStrings = s.decode(WINDOWS_ENCODING)
        cp['Clipboard'] = {
            'Strings': clipboardStrings
        }
        with open(self.iniFilename, 'w') as f:
            cp.write(f)
        root.destroy()

    def configured(self, event=None):
        self.update()
    
    def update(self):
        if self.afterId != None:
            root.after_cancel(self.afterId)
        s = ''
        try:
            s = root.clipboard_get()
        except:
            pass
        if s != '' and s != self.clipboardContent:
            list = self.listboxMain.get(0, tkinter.END)
        if s in list:
            shouldDelete = list.index(s)
            self.listboxMain.delete(shouldDelete, shouldDelete)
        self.clipboardcontent = s
        self.listboxMain.insert(0 ,s)
        if self.currentSelectionWillBeTop:
            self.listboxMain.select_set(0)
            self.currentSelectionWillBeTop = False
        self.afterId = root.after(INTERVAL, self.update)

    def menuEditCopy(self):
        self.updateClipboard(self.listboxMain.get(self.listboxMain.curselection()))
        self.currentSelectionWillBeTop = True

    def updateClipboard(self, newData):
        if newData != "":
            root.clipboard_clear()
            root.clipboard_append(newData)

    def menuEditCopyALL(self):
        toClipboard = ''
        for s in self.listboxMain.get(0, tkinter.END):
            toClipboard += s
        self.updateClipboard(toClipboard)

    def menuEditCopyAllSorted(self):
        toClipboard = ''    
        for s in sorted(self.listboxMain.get(0, tkinter.END)):
            toClipboard += s
        self.updateClipboard(toClipboard)

    def menuEditDelete(self, event=None):
        if self.listboxMain.curselection():
            self.listboxMain.delete(self.listboxMain.curselection())

    def menuEditDeleteAll(self):
        if messagebox.askyesno(self.__class__.__name__, '全項目を削除しますか?'):
            self.lostboxMain.delete(0, tkinter.END)

    def menuEditOpenWeb(self):
        webbrowser.open(self.listboxMain.get(self.listboxMain.curselection()))
                        
    def menuSettingFontBigger(self, event=None):
        self.fontsize += 2
        self.listboxMain.config(font=(FONT, self.fontsize))

    def menuSettingFontSmaller(self, event=None):
        if self.fontsize > 8:
            self.fontsize -= 2
            self.listboxMain.config(font=(FONT, self.fontsize))

    def menuHelpOpenWeb(self):
        helpFilePath = os.path.dirname(__file__) + os.sep + 'help.html'
        if os.path.isfile(helpFilePath):
            helpFilePath = 'file:///' + helpFilePath.replace(os.sep, '/')
            webbrowser.open(helpFilePath)
        else:
            messagebox.showerror(self.__class__.__name__, helpFilePath + 'がありません')
        
    def menuHelpVersion(self):
        s = self.__class__.__name__
        s += '@2025 Hideo Harada\n'
        s += ' Version 0.01(2025/06/22)\n'
        s += 'with Python ' + sys.version
        messagebox.showinfo(self.__class__.__name__, s)


root = tkinter.Tk()
TextClipper(root)
root.mainloop()