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
## Class home
###########################################################################

class home ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Welcome", pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Read.in", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Forte" ) )
		self.m_staticText1.SetForegroundColour( wx.Colour( 251, 91, 96 ) )

		fgSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Bahnschrift" ) )
		self.m_staticText2.SetForegroundColour( wx.Colour( 143, 170, 239 ) )

		fgSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )


		bSizer3.Add( fgSizer2, 1, wx.EXPAND, 5 )

		self.btnKatalog = wx.Button( self, wx.ID_ANY, u"Katalog", wx.DefaultPosition, wx.Size( 200,-1 ), wx.BORDER_NONE )
		self.btnKatalog.SetFont( wx.Font( 20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Goudy Old Style" ) )
		self.btnKatalog.SetForegroundColour( wx.Colour( 255, 128, 128 ) )
		self.btnKatalog.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.btnKatalog.SetMaxSize( wx.Size( 200,-1 ) )

		bSizer3.Add( self.btnKatalog, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.btnOrder = wx.Button( self, wx.ID_ANY, u"Order", wx.DefaultPosition, wx.Size( 200,-1 ), wx.BORDER_NONE )
		self.btnOrder.SetFont( wx.Font( 20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Goudy Old Style" ) )
		self.btnOrder.SetForegroundColour( wx.Colour( 255, 128, 128 ) )
		self.btnOrder.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer3.Add( self.btnOrder, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btnKeranjang = wx.Button( self, wx.ID_ANY, u"Keranjang", wx.DefaultPosition, wx.Size( 200,-1 ), wx.BORDER_NONE )
		self.btnKeranjang.SetFont( wx.Font( 20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Goudy Old Style" ) )
		self.btnKeranjang.SetForegroundColour( wx.Colour( 255, 128, 128 ) )
		self.btnKeranjang.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer3.Add( self.btnKeranjang, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btnLogout = wx.Button( self, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.Size( 200,-1 ), wx.BORDER_NONE )
		self.btnLogout.SetFont( wx.Font( 20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Goudy Old Style" ) )
		self.btnLogout.SetForegroundColour( wx.Colour( 255, 128, 128 ) )
		self.btnLogout.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer3.Add( self.btnLogout, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnKatalog.Bind( wx.EVT_BUTTON, self.btnKatalogOnButtonClick )
		self.btnOrder.Bind( wx.EVT_BUTTON, self.btnOrderOnButtonClick )
		self.btnKeranjang.Bind( wx.EVT_BUTTON, self.btnKeranjangOnButtonClick )
		self.btnLogout.Bind( wx.EVT_BUTTON, self.btnLogoutOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnKatalogOnButtonClick( self, event ):
		event.Skip()

	def btnOrderOnButtonClick( self, event ):
		event.Skip()

	def btnKeranjangOnButtonClick( self, event ):
		event.Skip()

	def btnLogoutOnButtonClick( self, event ):
		event.Skip()


