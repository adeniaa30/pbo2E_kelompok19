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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 334,250 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		self.loguser = wx.StaticText( self, wx.ID_ANY, u"LOGIN USER", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.loguser.Wrap( -1 )

		bSizer1.Add( self.loguser, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.usernameuser = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.usernameuser.Wrap( -1 )

		gSizer1.Add( self.usernameuser, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

		self.passuser = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.passuser.Wrap( -1 )

		gSizer1.Add( self.passuser, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl3, 0, wx.ALL, 5 )


		self.m_panel2.SetSizer( gSizer1 )
		self.m_panel2.Layout()
		gSizer1.Fit( self.m_panel2 )
		bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel5 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )

		self.btnloguser = wx.Button( self.m_panel3, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnloguser, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_panel6 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.btnregister = wx.Button( self.m_panel6, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btnregister, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.btnlupapass = wx.Button( self.m_panel6, wx.ID_ANY, u"Lupa Password?", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btnlupapass, 0, wx.ALL, 5 )


		self.m_panel6.SetSizer( gSizer2 )
		self.m_panel6.Layout()
		gSizer2.Fit( self.m_panel6 )
		bSizer2.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel3.SetSizer( bSizer2 )
		self.m_panel3.Layout()
		bSizer2.Fit( self.m_panel3 )
		bSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )

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


