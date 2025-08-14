import configparser, os, sys, tkinter, webbrowser
from tkinter import font, messagebox, scrolledtext, simpledialog

HAN_DIGIT = '0123456789'
ZEN_DIGIT ='０１２３４５６７８９'
HAN_ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ZEN_ALPHABET = 'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ'

class TextFilter:
    def __init__(self, root:tkinter.Tk):
        root.title(self.__class__.__name__)
        self.iniFilename = os.path.abspath(
            __file__).replace('.py', '.ini')
        clientX = '200'
        clientY = '200'
        clientHeight = '100'
        cliientWidth = '300'
        global fontFamily
        fontFamily = 'Courier New'
        self.fontSize = 20
        cp = configparser.ConfigParser()
        try:
            cp.read(self.iniFilename)
            clientX = cp['Client']['X']
            clientY = cp['Client']['Y']
            clientHeight = cp['Client']['Height']
            cliientWidth = cp['Client']['Width']
            self.fontSize = int(cp['Font']['Size'])
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
        menuEdit = tkinter.Menu()
        menu.add_cascade(menu=menuEdit, label='編集(E)', underline=3)
        menuEdit.add_command(label='全切り取り(X)', underline=6,
            command=self.menuEditCUt)
        menuEdit.add_command(label='全コピー(C)', underline=6,
            command=self.menuEditCopy)
        menuEdit.add_command(label='全貼り付け(V)', underline=6,
            command=self.menuEditPaste)
        menuEdit.add_command(label='変換1(1)', underline=4,
            command=self.menuEditConvert1)
        menuSetting = tkinter.Menu()
        menu.add_cascade(menu=menuSetting, label='設定(S)', underline=3)
        menuSetting.add_command(label='フォント(F)', underline=5,   
            command=self.menuSettingFontFamily)
        menuSetting.add_command(label='フォントを大きく(B)', underline=9,
            command=self.menuSettingFontBigger, accelerator='ALT+F2')
        menuSetting.add_command(label='フォントを小さく(S)', underline=9,
            command=self.menuSettingFontSmaller, accelerator='ALT+F1')
        menuHelp = tkinter.Menu()
        menu.add_cascade(menu=menuHelp, label='ヘルプ(H)', underline=4)
        menuHelp.add_command(label='ヘルプファイルを開く(O)',
            underline=10, command=self.menuHelpOpenWeb)
        menuHelp.add_command(label='バージョン情報(V)',
            underline=8, command=self.menuHelpVersion)
        root['menu'] = menu
        #root.bind_all('<Alt-F4>', self.menuFileExit)
        root.bind_all('<Alt-F2>', self.menuSettingFontBigger)
        root.bind_all('<Alt-F1>', self.menuSettingFontSmaller)    
        self.text = scrolledtext.ScrolledText(font=(fontFamily, self.fontSize))
        self.text.pack(expand=1, fill=tkinter.BOTH)

    def menuFileExit(self, event=None):
        cp = configparser.ConfigParser()
        cp['Client'] = {
            'X': str(root.winfo_x()),
            'Y': str(root.winfo_y()),
            'Height': str(root.winfo_height()),
            'Width': str(root.winfo_width())
        }
        cp['Font'] = {
            'Family': str(fontFamily),
            'Size': str(self.fontSize)
        }
        with open(self.iniFilename, 'w') as f:
            cp.write(f)
        root.destroy()    

    def menuEditCUt(self):
        self.menuEditCopy()
        self.text.delete('1.0', 'end')

    def menuEditCopy(self):
        self.text.clipboard_clear()
        self.text.clipboard_append(self.text.get('1.0', 'end-1c'))

    def menuEditPaste(self):
        try:
            s:str = self.text.clipboard_get()
            self.text.delete('1.0', 'end')
            self.text.insert('insert', s)
        except:
            messagebox.showerror(self.__class__.__name__, 'クリップボードの内容が文字列ではありません')

    def menuEditConvert1(self):
        s = self.text.get('1.0', 'end-1c')
        table = str.maketrans( ZEN_DIGIT + ZEN_ALPHABET , HAN_DIGIT + HAN_ALPHABET)
        s = s.translate(table)
        s = s.replace('.', '。')
        s = s.replace(',', '、')
        s = s.replace('ウェア', 'ウエア')
        self.text.delete('1.0', 'end')
        self.text.insert('1.0', s)  

    def menuSettingFontFamily(self):
        fd = FontDialog(root)
        f = fd.fontSelected
        if f != '':
            self.text.config(font=(f, self.fontSize))
            global fontFamily
            fontFamily = f

    def menuSettingFontBigger(self, event=None):
        if self.fontSize < 300:self.fontSize += 10
        self.text.config(font=(fontFamily, self.fontSize))

    def menuSettingFontSmaller(self, event=None):
        if self.fontSize >= 20:self.fontSize -= 10
        self.text.config(font=(fontFamily, self.fontSize))         

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

class FontDialog(simpledialog.Dialog):
    fontSelected = ''
    def __init__(self, parent, title='フォント設定'):
        super(FontDialog, self).__init__(parent=parent, title=title)

    def body(self, parent):
        values = tkinter.StringVar(value=FONTS)
        self.listbox = tkinter.Listbox(parent, listvariable=values, width='50')
        self.listbox.grid(row=0, column=1)
        scrollbar = tkinter.Scrollbar(parent, orient=tkinter.VERTICAL, command=self.listbox.yview, width= 30)
        self.listbox['yscrollcommand'] = scrollbar.set
        scrollbar.grid(row=0, column=1, sticky=tkinter.N + tkinter.S)
        try:
            self.listbox.selection_set(FONTS.index(fontFamily))
        except:
            pass
    def apply(self):
        self.fontSelected = self.listbox.get(self.listbox.curselection())
    
fontFamily: str
root = tkinter.Tk()
FONTS = list(font.families(root))
TextFilter(root)
root.mainloop()

