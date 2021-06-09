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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Home Page", pos = wx.DefaultPosition, size = wx.Size( 433,243 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel14 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14.Add( self.m_panel14, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Read.in merupakan sebuah platform yang menjual \nberbagai macam jenis buku. Happy Shopping!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer14.Add( self.m_staticText11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Login sebagai?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer14.Add( self.m_staticText10, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_panel15 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		self.btnuser = wx.Button( self.m_panel15, wx.ID_ANY, u"User", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.btnuser, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_button12 = wx.Button( self.m_panel15, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button12, 0, wx.ALIGN_LEFT|wx.ALL, 5 )


		self.m_panel15.SetSizer( gSizer6 )
		self.m_panel15.Layout()
		gSizer6.Fit( self.m_panel15 )
		bSizer14.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel16 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14.Add( self.m_panel16, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer14 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnuser.Bind( wx.EVT_BUTTON, self.btnuserOnButtonClick )
		self.m_button12.Bind( wx.EVT_BUTTON, self.m_button12OnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnuserOnButtonClick( self, event ):
		event.Skip()

	def m_button12OnButtonClick( self, event ):
		event.Skip()



