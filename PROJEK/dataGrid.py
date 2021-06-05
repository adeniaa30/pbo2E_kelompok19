# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class tabelGrid
###########################################################################

class tabelGrid ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Katalog", pos = wx.DefaultPosition, size = wx.Size( 850,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.tabel = wx.grid.Grid( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 630,-1 ), 0 )

		# Grid
		self.tabel.CreateGrid( 11, 7 )
		self.tabel.EnableEditing( True )
		self.tabel.EnableGridLines( True )
		self.tabel.EnableDragGridSize( False )
		self.tabel.SetMargins( 0, 0 )

		# Columns
		self.tabel.SetColSize( 0, 167 )
		self.tabel.SetColSize( 1, 80 )
		self.tabel.SetColSize( 2, 80 )
		self.tabel.SetColSize( 3, 71 )
		self.tabel.SetColSize( 4, 59 )
		self.tabel.SetColSize( 5, 39 )
		self.tabel.SetColSize( 6, 61 )
		self.tabel.EnableDragColMove( False )
		self.tabel.EnableDragColSize( True )
		self.tabel.SetColLabelSize( 30 )
		self.tabel.SetColLabelValue( 0, u"Judul" )
		self.tabel.SetColLabelValue( 1, u"Penerbit" )
		self.tabel.SetColLabelValue( 2, u"Penulis" )
		self.tabel.SetColLabelValue( 3, u"Kategori" )
		self.tabel.SetColLabelValue( 4, u"Tahun" )
		self.tabel.SetColLabelValue( 5, u"Stok" )
		self.tabel.SetColLabelValue( 6, u"Harga" )
		self.tabel.SetColLabelValue( 7, u"Hapus Data" )
		self.tabel.SetColLabelValue( 8, u"Edit Data" )
		self.tabel.SetColLabelValue( 9, wx.EmptyString )
		self.tabel.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel.EnableDragRowSize( True )
		self.tabel.SetRowLabelSize( 50 )
		self.tabel.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabel.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_TOP )
		fgSizer1.Add( self.tabel, 0, wx.ALIGN_CENTER|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.btnTampil = wx.Button( self.m_panel1, wx.ID_ANY, u"Tampilkan", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.btnTampil.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer4.Add( self.btnTampil, 0, wx.ALL, 5 )

		self.btnTambah = wx.Button( self.m_panel1, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.btnTambah.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btnTambah.SetBackgroundColour( wx.Colour( 78, 248, 150 ) )

		bSizer4.Add( self.btnTambah, 0, wx.ALL, 5 )

		self.btnEdit = wx.Button( self.m_panel1, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.btnEdit.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btnEdit.SetBackgroundColour( wx.Colour( 87, 192, 249 ) )

		bSizer4.Add( self.btnEdit, 0, wx.ALL, 5 )

		self.btnHapus = wx.Button( self.m_panel1, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.btnHapus.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btnHapus.SetBackgroundColour( wx.Colour( 247, 83, 87 ) )

		bSizer4.Add( self.btnHapus, 0, wx.ALL, 5 )

		self.bttnOrder = wx.Button( self.m_panel1, wx.ID_ANY, u"Order", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.bttnOrder.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.bttnOrder.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.bttnOrder.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.bttnOrder, 0, wx.ALL, 5 )

		self.m_panel3 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )

		self.btnMenu = wx.Button( self.m_panel1, wx.ID_ANY, u"Menu", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.btnMenu.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btnMenu.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btnMenu.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer4.Add( self.btnMenu, 0, wx.ALL, 5 )


		fgSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( fgSizer1 )
		self.m_panel1.Layout()
		fgSizer1.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"Daftar Buku", False )
		self.m_panel31 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.tabelPen = wx.grid.Grid( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )

		# Grid
		self.tabelPen.CreateGrid( 15, 3 )
		self.tabelPen.EnableEditing( True )
		self.tabelPen.EnableGridLines( True )
		self.tabelPen.EnableDragGridSize( False )
		self.tabelPen.SetMargins( 0, 0 )

		# Columns
		self.tabelPen.SetColSize( 0, 125 )
		self.tabelPen.SetColSize( 1, 88 )
		self.tabelPen.SetColSize( 2, 102 )
		self.tabelPen.EnableDragColMove( False )
		self.tabelPen.EnableDragColSize( True )
		self.tabelPen.SetColLabelSize( 30 )
		self.tabelPen.SetColLabelValue( 0, u"Nama" )
		self.tabelPen.SetColLabelValue( 1, u"No.Telp" )
		self.tabelPen.SetColLabelValue( 2, u"Kota" )
		self.tabelPen.SetColLabelValue( 3, wx.EmptyString )
		self.tabelPen.SetColLabelValue( 4, wx.EmptyString )
		self.tabelPen.SetColLabelValue( 5, u"No.Telp" )
		self.tabelPen.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelPen.EnableDragRowSize( True )
		self.tabelPen.SetRowLabelSize( 80 )
		self.tabelPen.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabelPen.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer2.Add( self.tabelPen, 0, wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.tampilPen = wx.Button( self.m_panel31, wx.ID_ANY, u"Tampilkan", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.tampilPen.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer3.Add( self.tampilPen, 0, wx.ALL, 5 )

		self.tambahPen = wx.Button( self.m_panel31, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.tambahPen.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.tambahPen.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		bSizer3.Add( self.tambahPen, 0, wx.ALL, 5 )

		self.hapusPen = wx.Button( self.m_panel31, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.hapusPen.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.hapusPen.SetBackgroundColour( wx.Colour( 255, 70, 70 ) )

		bSizer3.Add( self.hapusPen, 0, wx.ALL, 5 )

		self.btnRefresh = wx.Button( self.m_panel31, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.btnRefresh.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btnRefresh.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btnRefresh.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer3.Add( self.btnRefresh, 0, wx.ALL, 5 )

		self.m_panel5 = wx.Panel( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )

		self.btnMenu2 = wx.Button( self.m_panel31, wx.ID_ANY, u"Menu", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.btnMenu2.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btnMenu2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btnMenu2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer3.Add( self.btnMenu2, 0, wx.ALL, 5 )

		self.m_panel7 = wx.Panel( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel8 = wx.Panel( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel6 = wx.Panel( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel4 = wx.Panel( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )


		fgSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.m_panel31.SetSizer( fgSizer2 )
		self.m_panel31.Layout()
		fgSizer2.Fit( self.m_panel31 )
		self.m_notebook1.AddPage( self.m_panel31, u"Daftar Penulis", True )

		bSizer2.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tabel.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.selectCell )
		self.btnTampil.Bind( wx.EVT_BUTTON, self.btnTampilOnButtonClick )
		self.btnTambah.Bind( wx.EVT_BUTTON, self.btnTambahOnButtonClick )
		self.bttnOrder.Bind( wx.EVT_BUTTON, self.bttnOrderOnButtonClick )
		self.btnMenu.Bind( wx.EVT_BUTTON, self.btnMenuOnButtonClick )
		self.tampilPen.Bind( wx.EVT_BUTTON, self.tampilPenOnButtonClick )
		self.tambahPen.Bind( wx.EVT_BUTTON, self.tambahPenOnButtonClick )
		self.hapusPen.Bind( wx.EVT_BUTTON, self.hapusPenOnButtonClick )
		self.btnRefresh.Bind( wx.EVT_BUTTON, self.btnRefreshOnButtonClick )
		self.btnMenu2.Bind( wx.EVT_BUTTON, self.btnMenu2OnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def selectCell( self, event ):
		event.Skip()

	def btnTampilOnButtonClick( self, event ):
		event.Skip()

	def btnTambahOnButtonClick( self, event ):
		event.Skip()

	def bttnOrderOnButtonClick( self, event ):
		event.Skip()

	def btnMenuOnButtonClick( self, event ):
		event.Skip()

	def tampilPenOnButtonClick( self, event ):
		event.Skip()

	def tambahPenOnButtonClick( self, event ):
		event.Skip()

	def hapusPenOnButtonClick( self, event ):
		event.Skip()

	def btnRefreshOnButtonClick( self, event ):
		event.Skip()

	def btnMenu2OnButtonClick( self, event ):
		event.Skip()


