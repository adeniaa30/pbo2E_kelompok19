import order
import sqlite3
import wx

def create(parent):
	return order.MyFrame2(parent)

class orderBuku(order.MyFrame2):
    con = sqlite3.connect('tokobuku.db')
    cursor = con.cursor()

    def __init__(self, parent):
        order.MyFrame2.__init__(self, parent)
        self.row = 0

    def execQuery(self, query, retVal=False):
        self.cursor.execute(query)
        hasil = self.cursor.fetchall()
        self.con.commit()
        if retVal:
            return hasil

    def btnKeranjangOnButtonClick( self, event ):
        judul_barang = self.inputJudul.GetValue()
        jumlah_barang = str(self.inputJml.GetValue())
        self.query = """select judul, harga from buku where judul = ?"""
        cursor.execute(self.query, (judul_barang,))
        for row in cursor.fetchall():
            keranjang().setKeranjang(judul_barang, jumlah_barang, row[1])
        if (wx.OK):
            self.inputJudul.SetValue("")
            self.inputJml.SetValue("")

con = sqlite3.connect('tokobuku.db')
cursor = con.cursor()

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

class buku(manager):
    def setBuku(self, id_buku, judul, id_penerbit, id_penulis, id_kategori, id_transaksi, tahun, stok, harga):
        self.query = 'INSERT INTO Buku (id_buku, judul, id_penerbit, id_penulis, id_kategori, id_transaksi, tahun, stok, harga) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\');'
        self.query = self.query % (id_buku, judul, id_penerbit, id_penulis, id_kategori, id_transaksi, tahun, stok, harga)
        self.execQuery(self.query)
        print('\n')
        print('Berhasil Ditambahkan')
        print('\n')
    def getBuku(self):
        self.query = 'select * from buku'
        cursor.execute(self.query)
        hasil = cursor.fetchall()

class keranjang(buku):
    def setKeranjang(self, judul_barang, jumlah_barang, harga_buku):
        self.q_keranjang = 'INSERT INTO Keranjang (judul_barang, jumlah_barang, harga_buku) VALUES (\'%s\', \'%s\', \'%s\');'
        self.q_keranjang = self.q_keranjang % (judul_barang, jumlah_barang, harga_buku)
        self.execQuery(self.q_keranjang)

        wx.MessageBox("berhasil memasukkan keranjang", "Berhasil", wx.OK | wx.ICON_INFORMATION)
        
    
    def getKeranjang(self):
        self.q_keranjang = 'select * from Keranjang'
        cursor.execute(self.q_keranjang)
        hasil = cursor.fetchall()
        for row in hasil:
            print('Judul Buku : ', row[1])
            print('Jumlah Barang Dibeli : ', row[2])
            print('Harga Buku : ', row[3])
            print('\n')
    




app = wx.App()
frame = orderBuku(parent=None)
frame.Show()
app.MainLoop()