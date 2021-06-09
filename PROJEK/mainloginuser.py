import LoginUserReal
import sqlite3
import wx

con = sqlite3.connect('tokobuku.db')
cursor = con.cursor()

def create(parent):
	return LoginUserReal.MyFrame1(parent)

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

class login12(LoginUserReal.MyFrame1):
    def __init__(self, parent):
        LoginUserReal.MyFrame1.__init__(self, parent)
        
    def btnloguserOnButtonClick( self, event ):
        uname = self.inputUser.GetValue()
        pwd = self.inputPass.GetValue()
        query = """SELECT * from Akun where uname = ? and pwd = ?"""
        cursor.execute(query, (uname, pwd))
        if cursor.fetchall():
            wx.MessageBox("Login Berhasil!", "Login")
            import mainMenu
            self.frame2 = mainMenu.create(self)
            self.frame2.Show()
        else :
            wx.MessageBox("Error", "Login Gagal !")

    def btnregisterOnButtonClick( self, event ):
        import mainregister
        self.frame2 = mainregister.create(self)
        self.frame2.Show()


	# def btnlupapassOnButtonClick( self, event ):
	# 	event.Skip()



app = wx.App()
frame = login12(parent=None)
frame.Show()
app.MainLoop()