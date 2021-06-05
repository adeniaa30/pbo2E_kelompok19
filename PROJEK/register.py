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
## Class register
###########################################################################

class register ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Register", pos = wx.DefaultPosition, size = wx.Size( 522,346 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer4.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"REGISTRASI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer4.Add( self.m_staticText9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.nama = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama.Wrap( -1 )

		gSizer4.Add( self.nama, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.no = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Nomor Telfon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.no.Wrap( -1 )

		gSizer4.Add( self.no, 0, wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

		self.pass = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pass.Wrap( -1 )

		gSizer4.Add( self.pass, 0, wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer4.Add( self.m_textCtrl5, 0, wx.ALL, 5 )

		self.konpass = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Konfirmasi Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.konpass.Wrap( -1 )

		gSizer4.Add( self.konpass, 0, wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer4.Add( self.m_textCtrl6, 0, wx.ALL, 5 )


		self.m_panel10.SetSizer( gSizer4 )
		self.m_panel10.Layout()
		gSizer4.Fit( self.m_panel10 )
		bSizer4.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button8 = wx.Button( self.m_panel11, wx.ID_ANY, u"Daftar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button8, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_button9 = wx.Button( self.m_panel11, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button9, 0, wx.ALIGN_LEFT|wx.ALL, 5 )


		self.m_panel11.SetSizer( gSizer5 )
		self.m_panel11.Layout()
		gSizer5.Fit( self.m_panel11 )
		bSizer4.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel12 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )

		self.log = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.log, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


