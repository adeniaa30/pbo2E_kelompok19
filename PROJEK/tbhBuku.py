# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,502 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Tambah Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 22, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Goudy Old Style" ) )
		self.m_staticText2.SetForegroundColour( wx.Colour( 211, 120, 58 ) )

		bSizer4.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Masukkan ID Penerbit :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Goudy Old Style" ) )

		gSizer1.Add( self.m_staticText31, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.inputID = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		gSizer1.Add( self.inputID, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Masukkan Judul Buku :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Goudy Old Style" ) )

		gSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.inputJudul = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,30 ), 0 )
		gSizer1.Add( self.inputJudul, 0, wx.ALL, 5 )

		self.m_staticText321 = wx.StaticText( self, wx.ID_ANY, u"Masukkan Penerbit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText321.Wrap( -1 )

		self.m_staticText321.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Goudy Old Style" ) )

		gSizer1.Add( self.m_staticText321, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.inputPenerbit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,30 ), 0 )
		gSizer1.Add( self.inputPenerbit, 0, wx.ALL, 5 )

		self.m_staticText311 = wx.StaticText( self, wx.ID_ANY, u"Masukkan Penulis:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText311.Wrap( -1 )

		self.m_staticText311.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Goudy Old Style" ) )

		gSizer1.Add( self.m_staticText311, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.inputPenulis = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,30 ), 0 )
		gSizer1.Add( self.inputPenulis, 0, wx.ALL, 5 )

		self.m_staticText3111 = wx.StaticText( self, wx.ID_ANY, u"Masukkan Kategori :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3111.Wrap( -1 )

		self.m_staticText3111.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Goudy Old Style" ) )

		gSizer1.Add( self.m_staticText3111, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.inputKategori = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,30 ), 0 )
		gSizer1.Add( self.inputKategori, 0, wx.ALL, 5 )

		self.m_staticText31111 = wx.StaticText( self, wx.ID_ANY, u"Masukkan Tahun :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31111.Wrap( -1 )

		self.m_staticText31111.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Goudy Old Style" ) )

		gSizer1.Add( self.m_staticText31111, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.inputTahun = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,30 ), 0 )
		gSizer1.Add( self.inputTahun, 0, wx.ALL, 5 )

		self.m_staticText311111 = wx.StaticText( self, wx.ID_ANY, u"Masukkan Stok :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText311111.Wrap( -1 )

		self.m_staticText311111.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Goudy Old Style" ) )

		gSizer1.Add( self.m_staticText311111, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.inputStok = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,30 ), 0 )
		gSizer1.Add( self.inputStok, 0, wx.ALL, 5 )

		self.m_staticText3111111 = wx.StaticText( self, wx.ID_ANY, u"Masukkan Harga :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3111111.Wrap( -1 )

		self.m_staticText3111111.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Goudy Old Style" ) )

		gSizer1.Add( self.m_staticText3111111, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.inputHarga = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,30 ), 0 )
		gSizer1.Add( self.inputHarga, 0, wx.ALL, 5 )


		bSizer4.Add( gSizer1, 1, wx.EXPAND, 5 )

		self.m_panel13 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4.Add( self.m_panel13, 1, wx.EXPAND |wx.ALL, 5 )

		self.btnSimpan = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.Size( 100,30 ), wx.BORDER_NONE )
		self.btnSimpan.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.btnSimpan.SetBackgroundColour( wx.Colour( 132, 250, 75 ) )

		bSizer4.Add( self.btnSimpan, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel14 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4.Add( self.m_panel14, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel15 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel12 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnSimpan.Bind( wx.EVT_BUTTON, self.btnSimpanOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnSimpanOnButtonClick( self, event ):
		event.Skip()


