import menu
import sqlite3
import wx

con = sqlite3.connect('tokobuku.db')
cursor = con.cursor()

def create(parent):
	return menu.home(parent)

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

class myMenu(menu.home):
    def __init__(self, parent):
        menu.home.__init__(self, parent)

    def btnKatalogOnButtonClick( self, event ):
        import mainAwalUser
        self.frame2 = mainAwalUser.create(self)
        self.frame2.Show()
    
    def btnLogoutOnButtonClick( self, event ):
        import mainhome
        self.frame2 = mainhome.create(self)
        self.frame2.Show()
    
    def btnKeranjangOnButtonClick( self, event ):
        import mainKeranjang
        self.frame2 = mainKeranjang.create(self)
        self.frame2.Show()

	

app = wx.App()
frame = myMenu(parent=None)
frame.Show()
app.MainLoop()