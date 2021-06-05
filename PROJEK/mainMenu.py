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

def data_rows(self):
    self.query = 'select judul, id_penerbit, id_penulis, id_kategori, tahun, stok, harga from Buku'
    cursor.execute(self.query)
    hasil = cursor.fetchall()
    i = 0
    for r in hasil : 
        i += 1
    return i

class myMenu(menu.home):
    def __init__(self, parent):
        menu.home.__init__(self, parent)

    def btnKatalogOnButtonClick( self, event ):
        import main
        self.frame2 = main.create(self)
        self.frame2.Show()
    
    def btnLogoutOnButtonClick( self, event ):
        import loginForm
        self.frame2 = loginForm.create(self)
        self.frame2.Show()
	# def btnOrderOnButtonClick( self, event ):
	# 	event.Skip()
    
    def btnKeranjangOnButtonClick( self, event ):
        import mainKeranjang
        self.frame2 = mainKeranjang.create(self)
        self.frame2.Show()

	

app = wx.App()
frame = myMenu(parent=None)
frame.Show()
app.MainLoop()