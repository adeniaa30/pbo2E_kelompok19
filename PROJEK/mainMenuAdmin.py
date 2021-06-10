import menuAdmin
import wx
import sqlite3

con = sqlite3.connect('tokobuku.db')
cursor = con.cursor()

def create(parent):
	return menuAdmin.home(parent)

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

class admin(menuAdmin.home):
    def __init__(self, parent):
        menuAdmin.home.__init__(self, parent)

    def btnKatalogOnButtonClick( self, event ):
        import mainKatalogAdmin
        self.frame2 = mainKatalogAdmin.create(self)
        self.frame2.Show()
    
    def btnKeranjangOnButtonClick( self, event ):
        import mainKeranjang
        self.frame2 = mainKeranjang.create(self)
        self.frame2.Show()

    def btnLogoutOnButtonClick( self, event ):
        import mainhome
        self.frame2 = mainhome.create(self)
        self.frame2.Show()

app = wx.App()
frame = admin(parent=None)
frame.Show()
app.MainLoop()