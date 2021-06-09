import registeruser
import sqlite3
import wx

con = sqlite3.connect('tokobuku.db')
cursor = con.cursor()

def create(parent):
	return registeruser.MyFrame1(parent)

class manager:
    def __init__(self):
        self.con = sqlite3.connect('tokobuku.db')
        self.cursor = self.con.cursor()
    def execQuery(self, query, retVal=False):
        self.cursor.execute(query)
        hasil = self.cursor.fetchall()
        self.con.commit()
        if retVal:
            return hasil

class register(registeruser.MyFrame1):
    def __init__(self, parent):
        registeruser.MyFrame1.__init__(self, parent)
        
    def btndaftarOnButtonClick( self, event ):
        uname = self.inputUser.GetValue()
        pwd = self.inputPass.GetValue()
        self.query = 'INSERT INTO Akun (uname, pwd) VALUES (\'%s\', \'%s\');'
        self.query = self.query % (uname, pwd)
        cursor.execute(self.query)
        con.commit()
        wx.MessageBox("Anda berhasil ditambahkan", "berhasil !", wx.OK)
        for row in cursor.fetchall():
            daftar().setDaftar(uname, pwd)
        if (wx.OK):
            self.inputUser.SetValue("")
            self.inputPass.SetValue("")

    def btnbackloginOnButtonClick( self, event ):
        import mainloginuser
        self.frame2 = mainloginuser.create(self)
        self.frame2.Show()
	
    def btncancelregisterOnButtonClick( self, event ):
        import mainloginuser
        self.frame2 = mainloginuser.create(self)
        self.frame2.Show()

class daftar(manager):
    def setDaftar(self, uname, pwd):
        self.query = 'INSERT INTO Akun (uname, pwd) VALUES (\'%s\', \'%s\');'
        self.query = self.query % (uname, pwd)
        self.execQuery(self.query)

        wx.MessageBox("Berhasil ditambahkan !", "berhasil !", wx.OK)


app = wx.App()
frame = register(parent=None)
frame.Show()
app.MainLoop()