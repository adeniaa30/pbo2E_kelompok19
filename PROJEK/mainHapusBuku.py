import menghapusBuku
import wx
import sqlite3

con = sqlite3.connect('tokobuku.db')
cursor = con.cursor()

def create(parent):
	return menghapusBuku.MyFrame2(parent)

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

class hapusBuku(menghapusBuku.MyFrame2):
    def __init__(self, parent):
        menghapusBuku.MyFrame2.__init__(self, parent)

    def btnSimpanOnButtonClick( self, event ):
        id_buku = self.inputID.GetValue()
        self.query = 'delete from Buku where id_buku = ?'
        cursor.execute(self.query, (id_buku,))
        con.commit()
        wx.MessageBox("Hapus berhasil ! Silahkan restar aplikasi", "Hapus", wx.OK)
        if wx.OK:
            self.inputID.SetValue("")

app = wx.App()
frame = hapusBuku(parent=None)
frame.Show()
app.MainLoop()