import tbhPenerbit
import wx
import sqlite3

con = sqlite3.connect('tokobuku.db')
cursor = con.cursor()

def create(parent):
	return tbhPenerbit.MyFrame2(parent)

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

class tambahPenerbit(tbhPenerbit.MyFrame2):
    def __init__(self, parent):
        tbhPenerbit.MyFrame2.__init__(self, parent)

    def btnSimpanOnButtonClick( self, event ):
        id_penerbit = self.inputID.GetValue()
        nama_penerbit = self.inputNama.GetValue()
        kota_penerbit = self.inputKota.GetValue()
        self.query = 'INSERT INTO Penerbit (id_penerbit, nama_penerbit, kota_penerbit) VALUES (\'%s\', \'%s\', \'%s\');'
        self.query = self.query % (id_penerbit, nama_penerbit, kota_penerbit)
        cursor.execute(self.query)
        con.commit()
        wx.MessageBox("Berhasil ditambahkan ! Silahkah restart aplikasi", "berhasil !", wx.OK)
        if (wx.OK):
            self.inputNama.SetValue("")
            self.inputID.SetValue("")
            self.inputKota.SetValue("")


app = wx.App()
frame = tambahPenerbit(parent=None)
frame.Show()
app.MainLoop()