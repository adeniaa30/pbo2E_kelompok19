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


		fgSizer1.Add( gSizer2, 1, wx.ALL, 5 )


		self.m_panel1.SetSizer( fgSizer1 )
		self.m_panel1.Layout()
		fgSizer1.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"Daftar Buku", True )

		bSizer2.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )


		bSizer2.Add( gSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tabel.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.tabelOnGridCmdSelectCell )
		self.bttnOrder.Bind( wx.EVT_BUTTON, self.bttnOrderOnButtonClick )
		self.btnMenu.Bind( wx.EVT_BUTTON, self.btnMenuOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tabelOnGridCmdSelectCell( self, event ):
		event.Skip()

	def bttnOrderOnButtonClick( self, event ):
		event.Skip()

	def btnMenuOnButtonClick( self, event ):
		event.Skip()


