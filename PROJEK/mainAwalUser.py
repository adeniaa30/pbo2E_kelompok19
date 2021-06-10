import awalUser2
import wx
import sqlite3

con = sqlite3.connect('tokobuku.db')
cursor = con.cursor()

def create(parent):
	return awalUser2.tabelGrid(parent)

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

class userAwal(awalUser2.tabelGrid):
    def __init__(self, parent):
        awalUser2.tabelGrid.__init__(self, parent)
        self.btnTampilOnButtonClick(self)

    def btnTampilOnButtonClick( self, event ):
        self.query = 'select id_buku, judul, nama_penerbit, nama_penulis, nama_kategori, tahun, stok, harga from Buku'
        cursor.execute(self.query)
        hasil = cursor.fetchall()
        for i in range (0, len(hasil)):
            for j in range (0, 8):
                cell = hasil[i]
                self.tabel.SetCellValue(i,j,str(cell[j]))

    def bttnOrderOnButtonClick( self, event ):
        import mainOrder
        self.frame2 = mainOrder.create(self)
        self.frame2.Show()

    def btnMenuOnButtonClick( self, event ):
        import mainMenu
        self.frame2 = mainMenu.create(self)
        self.frame2.Show()

app = wx.App()
frame = userAwal(parent=None)
frame.Show()
app.MainLoop()