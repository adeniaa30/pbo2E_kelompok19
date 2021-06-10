# from PROJEK.mainTambahPenerbit import tambahPenerbit
import katalogAdmin
import wx
import sqlite3

con = sqlite3.connect('tokobuku.db')
cursor = con.cursor()

def create(parent):
	return katalogAdmin.tabelGrid(parent)

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

class katalog(katalogAdmin.tabelGrid):
    def __init__(self, parent):
        katalogAdmin.tabelGrid.__init__(self, parent)
        self.btnTampilOnButtonClick(self)
        self.tampilPenerbitOnButtonClick(self)
        self.tampilPenOnButtonClick(self)

    def tabelOnGridCmdSelectCell( self, event ):
        col = event.GetCol()
        row = event.GetRow()
        idBuku = str(self.tabel.GetCellValue(row,col))
        isi = self.inputID.SetValue(idBuku)

    def btnTampilOnButtonClick( self, event ): #tampil buku
        self.query = 'select id_buku, judul, nama_penerbit, nama_penulis, nama_kategori, tahun, stok, harga from Buku'
        cursor.execute(self.query)
        hasil = cursor.fetchall()
        for i in range (0, len(hasil)):
            for j in range (0, 8):
                cell = hasil[i]
                self.tabel.SetCellValue(i,j,str(cell[j]))
    
    def btnTambahBukuOnButtonClick( self, event ): #tambah buku
        import mainTambahBuku
        self.frame2 = mainTambahBuku.create(self)
        self.frame2.Show()

    def btnHapusBukuOnButtonClick( self, event ): #hapus buku
        import mainHapusBuku
        self.frame2 = mainHapusBuku.create(self)
        self.frame2.Show()

    def btnRefresh0OnButtonClick( self, event ): #refresh buku
        row = self.tabel.GetNumberRows() # row = 15
        col = self.tabel.GetNumberCols() # col = 3
        for i in range(0, row):
            for j in range(0, col):
                self.tabel.SetCellValue(i,j," ")
    
    def btnMenuOnButtonClick( self, event ): #balik ke menu admin awal
        import mainMenuAdmin
        self.frame2 = mainMenuAdmin.create(self)
        self.frame2.Show()

    def bttnOrderOnButtonClick( self, event ): #order
        import mainOrder
        self.frame2 = mainOrder.create(self)
        self.frame2.Show()

    def tampilPenOnButtonClick( self, event ): #tampilkan penulis
        self.query = 'select * from Penulis'
        cursor.execute(self.query)
        hasil = cursor.fetchall()
        for i in range (0, len(hasil)):
            for j in range (0, 4):
                cell = hasil[i]
                self.tabelPen.SetCellValue(i,j,str(cell[j]))

    def tambahPenOnButtonClick( self, event ): #tambah penulis
        import tambahPenulis
        self.frame2 = tambahPenulis.create(self)
        self.frame2.Show()

    def hapusPenOnButtonClick( self, event ): #hapus penulis
        import hapusPenulis
        self.frame2 = hapusPenulis.create(self)
        self.frame2.Show()
    
    def btnMenu2OnButtonClick( self, event ): #balik ke menu admin
        import mainMenuAdmin
        self.frame2 = mainMenuAdmin.create(self)
        self.frame2.Show()

    def btnRefreshOnButtonClick( self, event ): #refresh tabel
        row = self.tabelPen.GetNumberRows() # row = 15
        col = self.tabelPen.GetNumberCols() # col = 3
        for i in range(0, row):
            for j in range(0, col):
                self.tabelPen.SetCellValue(i,j," ")
    
    def tampilPenerbitOnButtonClick( self, event ): #tampil penerbit
        self.query = 'select * from Penerbit'
        cursor.execute(self.query)
        hasil = cursor.fetchall()
        for i in range (0, len(hasil)):
            for j in range (0, 3):
                cell = hasil[i]
                self.tabelPenerbit.SetCellValue(i,j,str(cell[j]))

    def tambahPenerbitOnButtonClick( self, event ): #tambah penerbit
        import mainTambahPenerbit
        self.frame2 = mainTambahPenerbit.create(self)
        self.frame2.Show()

    def hapusPenerbitOnButtonClick( self, event ): #hapus penerbit
        import mainHapusPenerbit
        self.frame2 = mainHapusPenerbit.create(self)
        self.frame2.Show()

    def refreshOnButtonClick( self, event ):
        row = self.tabelPenerbit.GetNumberRows() # row = 15
        col = self.tabelPenerbit.GetNumberCols() # col = 3
        for i in range(0, row):
            for j in range(0, col):
                self.tabelPenerbit.SetCellValue(i,j," ")
    
    def btnMenu3OnButtonClick( self, event ): #balik ke menu admin
        import mainMenuAdmin
        self.frame2 = mainMenuAdmin.create(self)
        self.frame2.Show()


app = wx.App()
frame = katalog(parent=None)
frame.Show()
app.MainLoop()