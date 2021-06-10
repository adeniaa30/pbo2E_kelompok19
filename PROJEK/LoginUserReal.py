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
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 324,314 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"LOGIN USER", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Candara" ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_panel6 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel7 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )

		self.loguser = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Username :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.loguser.Wrap( -1 )

		self.loguser.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gSizer1.Add( self.loguser, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.inputUser = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.inputUser, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Password :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.inputPass = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer1.Add( self.inputPass, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_panel9 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel2.SetSizer( gSizer1 )
		self.m_panel2.Layout()
		gSizer1.Fit( self.m_panel2 )
		bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.btnloguser = wx.Button( self.m_panel3, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.btnloguser.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btnloguser.SetBackgroundColour( wx.Colour( 52, 234, 243 ) )

		bSizer2.Add( self.btnloguser, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel3.SetSizer( bSizer2 )
		self.m_panel3.Layout()
		bSizer2.Fit( self.m_panel3 )
		bSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.btnregister = wx.Button( self, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.btnregister.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btnregister.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		gSizer2.Add( self.btnregister, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.btnlupapass = wx.Button( self, wx.ID_ANY, u"Lupa Password?", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		gSizer2.Add( self.btnlupapass, 0, wx.ALIGN_LEFT|wx.ALL, 5 )


		bSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )

		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnloguser.Bind( wx.EVT_BUTTON, self.btnloguserOnButtonClick )
		self.btnregister.Bind( wx.EVT_BUTTON, self.btnregisterOnButtonClick )
		self.btnlupapass.Bind( wx.EVT_BUTTON, self.btnlupapassOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnloguserOnButtonClick( self, event ):
		event.Skip()

	def btnregisterOnButtonClick( self, event ):
		event.Skip()

	def btnlupapassOnButtonClick( self, event ):
		event.Skip()


