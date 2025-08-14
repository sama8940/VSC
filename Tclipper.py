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
            cd.read(self.iniFilename)
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
        menuEdit.add_command(label='選択項目をwebブラウザーで開く(O)', underline=17, command=self.menuEditOpenWEb)
        menuSetting = tkinter.Menu()
        menu.add_cascade(menu=menuSetting, label='設定(S)', underline=3)
        menuSetting.add_command(label='文字を大きく(B)', underline=7, command=self.menuSettingsFontBiller, accelerator='B')
        menuSetting.add_command(label='文字を小さく(S)', underline=7, command=self.menuSettingsFontSmaller, accelerator='S')
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
        self.clipboardcontent = ''
        self.currentSelectionWillBeTop = False
        root.bind('<Configure>', self.configured)
        root.bind('<Delete>', self.menuEditDelete)
        root.bind('<b>', self.menuSettingFontBiller)
        root.bind('<s>', self.menuSettingFontSmaller)
    
    def menuFileExit(self):
        root.destroy()

root = tkinter.Tk()
TextClipper(root)
root.mainloop