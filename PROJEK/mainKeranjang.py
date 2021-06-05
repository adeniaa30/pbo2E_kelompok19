import keranjang
import sqlite3
import wx

con = sqlite3.connect('tokobuku.db')
cursor = con.cursor()

def create(parent):
	return keranjang.MyFrame2(parent)

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

class kjg(keranjang.MyFrame2):
    def __init__(self, parent):
        keranjang.MyFrame2.__init__(self, parent)

    def btnMenuOnButtonClick( self, event ):
        import mainMenu
        self.frame2 = mainMenu.create(self)
        self.frame2.Show()
    
    def btnTampilOnButtonClick( self, event ):
        self.query = 'select judul_barang, jumlah_barang, harga_buku from Keranjang'
        cursor.execute(self.query)
        hasil = cursor.fetchall()
        for i in range (0, len(hasil)):
            for j in range (0, 3):
                cell = hasil[i]
                self.tabelKjg.SetCellValue(i,j,str(cell[j]))

    def bttnCOOnButtonClick( self, event ):
        query = 'select sum(jumlah_barang * harga_buku) from Keranjang as total_pembayaran;'
        cursor.execute(query)
        hasil = cursor.fetchall()
        for row in hasil:
            self.outputTotal.SetValue(str(row[0]))
            # print('total yang harus dibayar adalah : ', row[0])
    
    def bttnBayarOnButtonClick( self, event ):
        query = 'DELETE FROM Keranjang;'
        cursor.execute(query)
        con.commit()
        wx.MessageBox("Barang Anda Berhasil di Check Out", "Terima Kasih", wx.OK)
        row = self.tabelKjg.GetNumberRows() # row = 10
        col = self.tabelKjg.GetNumberCols() # col = 3
        if wx.OK:
            for i in range(0, row):
                for j in range(0, col):
                    self.tabelKjg.SetCellValue(i,j," ")


            self.outputTotal.SetValue("")
            self.tabelKjg.SetCellValue(0,1," ")
            self.tabelKjg.SetCellValue(0,2," ")
            self.tabelKjg.SetCellValue(1,0," ")
            self.tabelKjg.SetCellValue(1,1," ")
            self.tabelKjg.SetCellValue(1,2," ")
            self.tabelKjg.SetCellValue(0,0," ")
        
    def tabelKjgOnGridCmdSelectCell( self, event ):
        col = event.GetCol()
        row = event.GetRow()
        print("col : ", col , "row : ", row)



app = wx.App()
frame = kjg(parent=None)
frame.Show()
app.MainLoop()