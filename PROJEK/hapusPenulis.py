import hapusPen
import dataGrid
import sqlite3
import wx

con = sqlite3.connect('tokobuku.db')
cursor = con.cursor()

def create(parent):
	return hapusPen.MyFrame2(parent)

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

class hapuspen(hapusPen.MyFrame2):
    def __init__(self, parent):
        hapusPen.MyFrame2.__init__(self, parent)

    def btnSimpanOnButtonClick( self, event ):
        nama_penulis = self.inputNama.GetValue()
        self.query = 'delete from Penulis where nama_penulis = ?'
        cursor.execute(self.query, (nama_penulis,))
        con.commit()
        wx.MessageBox("Hapus berhasil ! Silahkan restar aplikasi", "Hapus", wx.OK)
        if wx.OK:
            self.inputNama.SetValue("")
            

app = wx.App()
frame = hapuspen(parent=None)
frame.Show()
app.MainLoop()