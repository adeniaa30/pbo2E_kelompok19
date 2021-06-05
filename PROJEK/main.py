from os import close
import dataGrid
import sqlite3
import wx
import gettext
import string

con = sqlite3.connect('tokobuku.db')
cursor = con.cursor()

def create(parent):
	return dataGrid.tabelGrid(parent)

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

class grid(dataGrid.tabelGrid):
    def __init__(self, parent):
        dataGrid.tabelGrid.__init__(self, parent)
        self.row = 0
    
    def selectCell( self, event ):
        col = event.GetCol()
        row = event.GetRow()
        print("col : ", col , "row : ", row)

    def btnTampilOnButtonClick( self, event ):
        self.query = 'select judul, id_penerbit, id_penulis, id_kategori, tahun, stok, harga from Buku'
        cursor.execute(self.query)
        hasil = cursor.fetchall()
        for i in range (0, len(hasil)):
            for j in range (0, 7):
                cell = hasil[i]
                self.tabel.SetCellValue(i,j,str(cell[j]))
    
    def btnMenuOnButtonClick( self, event ):
        import mainMenu
        self.frame2 = mainMenu.create(self)
        self.frame2.Show()

    def bttnOrderOnButtonClick( self, event ):
        import mainOrder
        self.frame2 = mainOrder.create(self)
        self.frame2.Show()

    def tampilPenOnButtonClick( self, event ):
        self.query = 'select nama_penulis, telp_penulis, kota_penulis from Penulis'
        cursor.execute(self.query)
        hasil = cursor.fetchall()
        for i in range (0, len(hasil)):
            for j in range (0, 3):
                cell = hasil[i]
                self.tabelPen.SetCellValue(i,j,str(cell[j]))

    def tambahPenOnButtonClick( self, event ):
        import tambahPenulis
        self.frame2 = tambahPenulis.create(self)
        self.frame2.Show()

    def hapusPenOnButtonClick( self, event ):
        import hapusPenulis
        self.frame2 = hapusPenulis.create(self)
        self.frame2.Show()
    
    def btnMenu2OnButtonClick( self, event ):
        import mainMenu
        self.frame2 = mainMenu.create(self)
        self.frame2.Show()

    def btnRefreshOnButtonClick( self, event ):
        row = self.tabelPen.GetNumberRows() # row = 15
        col = self.tabelPen.GetNumberCols() # col = 3
        for i in range(0, row):
            for j in range(0, col):
                self.tabelPen.SetCellValue(i,j," ")

app = wx.App()
frame = grid(parent=None)
frame.Show()
app.MainLoop()