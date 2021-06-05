import tambahPen
import sqlite3
import wx

con = sqlite3.connect('tokobuku.db')
cursor = con.cursor()

def create(parent):
	return tambahPen.MyFrame2(parent)


class tambahpen(tambahPen.MyFrame2):
    def __init__(self, parent):
        tambahPen.MyFrame2.__init__(self, parent)

    def btnSimpanOnButtonClick( self, event):
        id_penulis = self.inputID.GetValue()
        nama_penulis = self.inputNama.GetValue()
        telp_penulis = str(self.inputTelp.GetValue())
        kota_penulis = self.inputKota.GetValue()
        self.query = 'INSERT INTO Penulis (id_penulis, nama_penulis, telp_penulis, kota_penulis) VALUES (\'%s\', \'%s\', \'%s\', \'%s\');'
        self.query = self.query % (id_penulis, nama_penulis, telp_penulis, kota_penulis)
        cursor.execute(self.query)
        con.commit()
        wx.MessageBox("Berhasil ditambahkan ! Silahkah restart aplikasi", "berhasil !", wx.OK)
        for row in cursor.fetchall():
            penulis().setPenulis(id_penulis, nama_penulis, telp_penulis, kota_penulis)
        if (wx.OK):
            self.inputNama.SetValue("")
            self.inputID.SetValue("")
            self.inputKota.SetValue("")
            self.inputTelp.SetValue("")

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

class penulis(manager):
    def setPenulis(self, id_penulis, nama_penulis, telp_penulis, kota_penulis):
        self.query = 'INSERT INTO Penulis (id_penulis, nama_penulis, telp_penulis, kota_penulis) VALUES (\'%s\', \'%s\', \'%s\', \'%s\');'
        self.query = self.query % (id_penulis, nama_penulis, telp_penulis, kota_penulis)
        self.execQuery(self.query)

        wx.MessageBox("Berhasil ditambahkan !", "berhasil !", wx.OK)


app = wx.App()
frame = tambahpen(parent=None)
frame.Show()
app.MainLoop()