import home2
import sqlite3
import wx

con = sqlite3.connect('tokobuku.db')
cursor = con.cursor()

def create(parent):
	return home.home(parent)

class home1(home2.home):
    def __init__(self, parent):
        home2.home.__init__(self, parent)
    
    def btnuserOnButtonClick( self, event ): #login user
        import mainloginuser
        self.frame2 = mainloginuser.create(self)
        self.frame2.Show()

    def btnAdminOnButtonClick( self, event ): #login admin
        import loginForm
        self.frame2 = loginForm.create(self)
        self.frame2.Show()
        
app = wx.App()
frame = home1(parent=None)
frame.Show()
app.MainLoop()
