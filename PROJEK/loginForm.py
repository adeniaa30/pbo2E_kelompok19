import login
import sqlite3
import wx

con = sqlite3.connect('tokobuku.db')
cursor = con.cursor()

def create(parent):
	return login.MyFrame2(parent)

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

class loginGui(login.MyFrame2):
    def __init__(self, parent):
        login.MyFrame2.__init__(self, parent)
    
    def loginOnButtonClick( self, event ):
        user = self.inputUser.GetValue()
        pwd = self.inputPass.GetValue()
        query = """SELECT * from akun_admin where uname_admin = ? and pass_admin = ?"""
        cursor.execute(query, (user, pwd))
        if cursor.fetchall():
            wx.MessageBox("Login Berhasil!", "Login")
            import mainMenuAdmin
            self.frame2 = mainMenuAdmin.create(self)
            self.frame2.Show()
        else :
            wx.MessageBox("Error", "Login Gagal !")
    


app = wx.App()
frame = loginGui(parent=None)
frame.Show()
app.MainLoop()