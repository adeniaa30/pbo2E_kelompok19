import tbhBuku
import wx
import sqlite3

con = sqlite3.connect('tokobuku.db')
cursor = con.cursor()

def create(parent):
	return tbhBuku.MyFrame2(parent)

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

class tambahBuku(tbhBuku.MyFrame2):
    def __init__(self, parent):
        tbhBuku.MyFrame2.__init__(self, parent)

    def btnSimpanOnButtonClick( self, event ):
        id_buku = self.inputID.GetValue()
        judul = self.inputJudul.GetValue()
        nama_penerbit = self.inputPenerbit.GetValue()
        nama_penulis = self.inputPenulis.GetValue()
        nama_kategori = self.inputKategori.GetValue()
        tahun = self.inputTahun.GetValue()
        stok = self.inputStok.GetValue()
        harga = self.inputHarga.GetValue()
        self.query = 'INSERT INTO Buku (id_buku, judul, nama_penerbit, nama_penulis, nama_kategori, tahun, stok, harga) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\');'
        self.query = self.query % (id_buku, judul, nama_penerbit, nama_penulis, nama_kategori, tahun, stok, harga)
        cursor.execute(self.query)
        con.commit()
        wx.MessageBox("Berhasil ditambahkan ! Silahkah restart aplikasi", "berhasil !", wx.OK)
        if (wx.OK):
            self.inputID.SetValue("")
            self.inputJudul.SetValue("")
            self.inputPenerbit.SetValue("")
            self.inputPenulis.SetValue("")
            self.inputKategori.SetValue("")
            self.inputTahun.SetValue("")
            self.inputStok.SetValue("")
            self.inputHarga.SetValue("")


app = wx.App()
frame = tambahBuku(parent=None)
frame.Show()
app.MainLoop()