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
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Keranjang", pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.tabelKjg = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )

		# Grid
		self.tabelKjg.CreateGrid( 10, 3 )
		self.tabelKjg.EnableEditing( True )
		self.tabelKjg.EnableGridLines( True )
		self.tabelKjg.EnableDragGridSize( False )
		self.tabelKjg.SetMargins( 0, 0 )

		# Columns
		self.tabelKjg.SetColSize( 0, 108 )
		self.tabelKjg.SetColSize( 1, 80 )
		self.tabelKjg.SetColSize( 2, 80 )
		self.tabelKjg.EnableDragColMove( False )
		self.tabelKjg.EnableDragColSize( True )
		self.tabelKjg.SetColLabelSize( 30 )
		self.tabelKjg.SetColLabelValue( 0, u"Judul" )
		self.tabelKjg.SetColLabelValue( 1, u"Jumlah" )
		self.tabelKjg.SetColLabelValue( 2, u"Harga" )
		self.tabelKjg.SetColLabelValue( 3, wx.EmptyString )
		self.tabelKjg.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelKjg.EnableDragRowSize( True )
		self.tabelKjg.SetRowLabelSize( 80 )
		self.tabelKjg.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabelKjg.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer3.Add( self.tabelKjg, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.btnMenu = wx.Button( self, wx.ID_ANY, u"Back To Menu", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		bSizer4.Add( self.btnMenu, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btnTampil = wx.Button( self, wx.ID_ANY, u"Tampilkan", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		bSizer4.Add( self.btnTampil, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.bttnCO = wx.Button( self, wx.ID_ANY, u"Chek Out", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		bSizer4.Add( self.bttnCO, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		fgSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Total :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		fgSizer3.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.outputTotal = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer3.Add( self.outputTotal, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		fgSizer3.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )

		self.bttnBayar = wx.Button( self, wx.ID_ANY, u"Bayar Sekarang", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.bttnBayar, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer3.Add( fgSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tabelKjg.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.tabelKjgOnGridCmdSelectCell )
		self.btnMenu.Bind( wx.EVT_BUTTON, self.btnMenuOnButtonClick )
		self.btnTampil.Bind( wx.EVT_BUTTON, self.btnTampilOnButtonClick )
		self.bttnCO.Bind( wx.EVT_BUTTON, self.bttnCOOnButtonClick )
		self.bttnBayar.Bind( wx.EVT_BUTTON, self.bttnBayarOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tabelKjgOnGridCmdSelectCell( self, event ):
		event.Skip()

	def btnMenuOnButtonClick( self, event ):
		event.Skip()

	def btnTampilOnButtonClick( self, event ):
		event.Skip()

	def bttnCOOnButtonClick( self, event ):
		event.Skip()

	def bttnBayarOnButtonClick( self, event ):
		event.Skip()


