import home
import sqlite3
import wx

con = sqlite3.connect('tokobuku.db')
cursor = con.cursor()

def create(parent):
	return home.home(parent)

class home1(home.home):
    def __init__(self, parent):
        home.home.__init__(self, parent)
        self.row = 0
    
    def btnuserOnButtonClick( self, event ):
        import mainloginuser
        self.frame2 = mainloginuser.create(self)
        self.frame2.Show()

    def m_button12OnButtonClick( self, event ):
        import loginForm
        self.frame2 = loginForm.create(self)
        self.frame2.Show()
        
app = wx.App()
frame = home1(parent=None)
frame.Show()
app.MainLoop()