import hapusPenerbit
import wx
import sqlite3

con = sqlite3.connect('tokobuku.db')
cursor = con.cursor()

def create(parent):
	return hapusPenerbit.MyFrame2(parent)

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

class hpsPenerbit(hapusPenerbit.MyFrame2):
    def __init__(self, parent):
       hapusPenerbit.MyFrame2.__init__(self, parent)
    
    def btnSimpanOnButtonClick( self, event ):
        nama_penerbit = self.inputNama.GetValue()
        self.query = 'delete from Penerbit where nama_penerbit = ?'
        cursor.execute(self.query, (nama_penerbit,))
        con.commit()
        wx.MessageBox("Hapus berhasil ! Silahkan restar aplikasi", "Hapus", wx.OK)
        if wx.OK:
            self.inputNama.SetValue("")

app = wx.App()
frame = hpsPenerbit(parent=None)
frame.Show()
app.MainLoop()