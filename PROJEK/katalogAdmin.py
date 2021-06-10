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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Katalog", pos = wx.DefaultPosition, size = wx.Size( 850,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.tabel = wx.grid.Grid( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 830,-1 ), 0 )

		# Grid
		self.tabel.CreateGrid( 15, 8 )
		self.tabel.EnableEditing( True )
		self.tabel.EnableGridLines( True )
		self.tabel.EnableDragGridSize( False )
		self.tabel.SetMargins( 0, 0 )

		# Columns
		self.tabel.SetColSize( 0, 44 )
		self.tabel.SetColSize( 1, 170 )
		self.tabel.SetColSize( 2, 136 )
		self.tabel.SetColSize( 3, 126 )
		self.tabel.SetColSize( 4, 66 )
		self.tabel.SetColSize( 5, 87 )
		self.tabel.SetColSize( 6, 61 )
		self.tabel.SetColSize( 7, 64 )
		self.tabel.EnableDragColMove( False )
		self.tabel.EnableDragColSize( True )
		self.tabel.SetColLabelSize( 30 )
		self.tabel.SetColLabelValue( 0, u"ID Buku" )
		self.tabel.SetColLabelValue( 1, u"Judul" )
		self.tabel.SetColLabelValue( 2, u"Penerbit" )
		self.tabel.SetColLabelValue( 3, u"Penulis" )
		self.tabel.SetColLabelValue( 4, u"Kategori" )
		self.tabel.SetColLabelValue( 5, u"Tahun" )
		self.tabel.SetColLabelValue( 6, u"Stok" )
		self.tabel.SetColLabelValue( 7, u"Harga" )
		self.tabel.SetColLabelValue( 8, wx.EmptyString )
		self.tabel.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel.AutoSizeRows()
		self.tabel.EnableDragRowSize( True )
		self.tabel.SetRowLabelSize( 50 )
		self.tabel.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabel.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_TOP )
		fgSizer1.Add( self.tabel, 0, wx.ALIGN_CENTER|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel15 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 5 )

		gSizer2 = wx.GridSizer( 0, 6, 0, 0 )

		self.btnTampil = wx.Button( self.m_panel1, wx.ID_ANY, u"Tampilkan", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.btnTampil.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		gSizer2.Add( self.btnTampil, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btnTambahBuku = wx.Button( self.m_panel1, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.btnTambahBuku.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btnTambahBuku.SetBackgroundColour( wx.Colour( 78, 248, 150 ) )

		gSizer2.Add( self.btnTambahBuku, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btnHapusBuku = wx.Button( self.m_panel1, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.btnHapusBuku.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btnHapusBuku.SetBackgroundColour( wx.Colour( 247, 83, 87 ) )

		gSizer2.Add( self.btnHapusBuku, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.bttnOrder = wx.Button( self.m_panel1, wx.ID_ANY, u"Order", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.bttnOrder.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.bttnOrder.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.bttnOrder.SetBackgroundColour( wx.Colour( 218, 240, 94 ) )

		gSizer2.Add( self.bttnOrder, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btnMenu = wx.Button( self.m_panel1, wx.ID_ANY, u"Menu", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.btnMenu.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btnMenu.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btnMenu.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		gSizer2.Add( self.btnMenu, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btnRefresh0 = wx.Button( self.m_panel1, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.btnRefresh0.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btnRefresh0.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btnRefresh0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		gSizer2.Add( self.btnRefresh0, 0, wx.ALL, 5 )


		fgSizer1.Add( gSizer2, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.m_panel1.SetSizer( fgSizer1 )
		self.m_panel1.Layout()
		fgSizer1.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"Daftar Buku", True )
		self.m_panel31 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.tabelPen = wx.grid.Grid( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.Size( 450,-1 ), 0 )

		# Grid
		self.tabelPen.CreateGrid( 15, 4 )
		self.tabelPen.EnableEditing( True )
		self.tabelPen.EnableGridLines( True )
		self.tabelPen.EnableDragGridSize( False )
		self.tabelPen.SetMargins( 0, 0 )

		# Columns
		self.tabelPen.SetColSize( 0, 44 )
		self.tabelPen.SetColSize( 1, 121 )
		self.tabelPen.SetColSize( 2, 102 )
		self.tabelPen.SetColSize( 3, 94 )
		self.tabelPen.EnableDragColMove( False )
		self.tabelPen.EnableDragColSize( True )
		self.tabelPen.SetColLabelSize( 30 )
		self.tabelPen.SetColLabelValue( 0, u"ID" )
		self.tabelPen.SetColLabelValue( 1, u"Nama" )
		self.tabelPen.SetColLabelValue( 2, u"No.Telp" )
		self.tabelPen.SetColLabelValue( 3, u"Kota" )
		self.tabelPen.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelPen.AutoSizeRows()
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
		self.m_notebook1.AddPage( self.m_panel31, u"Daftar Penulis", False )
		self.m_panel10 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer21 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.tabelPenerbit = wx.grid.Grid( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.Size( 380,-1 ), 0 )

		# Grid
		self.tabelPenerbit.CreateGrid( 15, 3 )
		self.tabelPenerbit.EnableEditing( True )
		self.tabelPenerbit.EnableGridLines( True )
		self.tabelPenerbit.EnableDragGridSize( False )
		self.tabelPenerbit.SetMargins( 0, 0 )

		# Columns
		self.tabelPenerbit.SetColSize( 0, 46 )
		self.tabelPenerbit.SetColSize( 1, 136 )
		self.tabelPenerbit.SetColSize( 2, 105 )
		self.tabelPenerbit.EnableDragColMove( False )
		self.tabelPenerbit.EnableDragColSize( True )
		self.tabelPenerbit.SetColLabelSize( 30 )
		self.tabelPenerbit.SetColLabelValue( 0, u"ID" )
		self.tabelPenerbit.SetColLabelValue( 1, u"Nama " )
		self.tabelPenerbit.SetColLabelValue( 2, u"Kota" )
		self.tabelPenerbit.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelPenerbit.AutoSizeRows()
		self.tabelPenerbit.EnableDragRowSize( True )
		self.tabelPenerbit.SetRowLabelSize( 80 )
		self.tabelPenerbit.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabelPenerbit.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer21.Add( self.tabelPenerbit, 0, wx.ALL, 5 )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		self.tampilPenerbit = wx.Button( self.m_panel10, wx.ID_ANY, u"Tampilkan", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.tampilPenerbit.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer31.Add( self.tampilPenerbit, 0, wx.ALL, 5 )

		self.tambahPenerbit = wx.Button( self.m_panel10, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.tambahPenerbit.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.tambahPenerbit.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		bSizer31.Add( self.tambahPenerbit, 0, wx.ALL, 5 )

		self.hapusPenerbit = wx.Button( self.m_panel10, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.hapusPenerbit.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.hapusPenerbit.SetBackgroundColour( wx.Colour( 255, 70, 70 ) )

		bSizer31.Add( self.hapusPenerbit, 0, wx.ALL, 5 )

		self.refresh = wx.Button( self.m_panel10, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.refresh.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.refresh.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.refresh.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer31.Add( self.refresh, 0, wx.ALL, 5 )

		self.m_panel51 = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31.Add( self.m_panel51, 1, wx.EXPAND |wx.ALL, 5 )

		self.btnMenu3 = wx.Button( self.m_panel10, wx.ID_ANY, u"Menu", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.btnMenu3.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btnMenu3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btnMenu3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer31.Add( self.btnMenu3, 0, wx.ALL, 5 )

		self.m_panel71 = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31.Add( self.m_panel71, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel81 = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31.Add( self.m_panel81, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel61 = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31.Add( self.m_panel61, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel41 = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31.Add( self.m_panel41, 1, wx.EXPAND |wx.ALL, 5 )


		fgSizer21.Add( bSizer31, 1, wx.EXPAND, 5 )


		self.m_panel10.SetSizer( fgSizer21 )
		self.m_panel10.Layout()
		fgSizer21.Fit( self.m_panel10 )
		self.m_notebook1.AddPage( self.m_panel10, u"Daftar Penerbit", False )

		bSizer2.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )


		bSizer2.Add( gSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tabel.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.tabelOnGridCmdSelectCell )
		self.btnTampil.Bind( wx.EVT_BUTTON, self.btnTampilOnButtonClick )
		self.btnTambahBuku.Bind( wx.EVT_BUTTON, self.btnTambahBukuOnButtonClick )
		self.btnHapusBuku.Bind( wx.EVT_BUTTON, self.btnHapusBukuOnButtonClick )
		self.bttnOrder.Bind( wx.EVT_BUTTON, self.bttnOrderOnButtonClick )
		self.btnMenu.Bind( wx.EVT_BUTTON, self.btnMenuOnButtonClick )
		self.btnRefresh0.Bind( wx.EVT_BUTTON, self.btnRefresh0OnButtonClick )
		self.tampilPen.Bind( wx.EVT_BUTTON, self.tampilPenOnButtonClick )
		self.tambahPen.Bind( wx.EVT_BUTTON, self.tambahPenOnButtonClick )
		self.hapusPen.Bind( wx.EVT_BUTTON, self.hapusPenOnButtonClick )
		self.btnRefresh.Bind( wx.EVT_BUTTON, self.btnRefreshOnButtonClick )
		self.btnMenu2.Bind( wx.EVT_BUTTON, self.btnMenu2OnButtonClick )
		self.tampilPenerbit.Bind( wx.EVT_BUTTON, self.tampilPenerbitOnButtonClick )
		self.tambahPenerbit.Bind( wx.EVT_BUTTON, self.tambahPenerbitOnButtonClick )
		self.hapusPenerbit.Bind( wx.EVT_BUTTON, self.hapusPenerbitOnButtonClick )
		self.refresh.Bind( wx.EVT_BUTTON, self.refreshOnButtonClick )
		self.btnMenu3.Bind( wx.EVT_BUTTON, self.btnMenu3OnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tabelOnGridCmdSelectCell( self, event ):
		event.Skip()

	def btnTampilOnButtonClick( self, event ):
		event.Skip()

	def btnTambahBukuOnButtonClick( self, event ):
		event.Skip()

	def btnHapusBukuOnButtonClick( self, event ):
		event.Skip()

	def bttnOrderOnButtonClick( self, event ):
		event.Skip()

	def btnMenuOnButtonClick( self, event ):
		event.Skip()

	def btnRefresh0OnButtonClick( self, event ):
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

	def tampilPenerbitOnButtonClick( self, event ):
		event.Skip()

	def tambahPenerbitOnButtonClick( self, event ):
		event.Skip()

	def hapusPenerbitOnButtonClick( self, event ):
		event.Skip()

	def refreshOnButtonClick( self, event ):
		event.Skip()

	def btnMenu3OnButtonClick( self, event ):
		event.Skip()


