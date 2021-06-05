# from wx.core import Frame
from wx.core import BRUSHSTYLE_SOLID, PENSTYLE_DOT_DASH, PENSTYLE_SOLID, Width
import noname
import wx


class gui(noname.MyFrame1):
    def __init__(self, parent):
        noname.MyFrame1.__init__(self,parent)
    
    def m_panel1OnPaint( self, event ):
        dc = wx.PaintDC(self.m_panel1)
        dc.SetPen(wx.Pen(wx.Colour(200,150,100), width=3, style=PENSTYLE_SOLID))
        dc.DrawLine(0,0,300,300)

        dc.SetPen(wx.Pen(wx.Colour(255,0,0), width=4, style=PENSTYLE_SOLID))
        dc.SetBrush(wx.Brush(wx.Colour(0,200,80), style=BRUSHSTYLE_SOLID))
        dc.DrawRectangle(250, 25, 200, 100)

        dc.SetPen(wx.Pen(wx.Colour(255,0,0), width=4, style=PENSTYLE_SOLID))
        dc.SetBrush(wx.Brush(wx.Colour(0,200,80), style=BRUSHSTYLE_SOLID))
        dc.DrawCircle(300, 200, 50)
           

app = wx.App()
frame = gui(parent=None)
frame.Show()
app.MainLoop()
