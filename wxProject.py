import wx

from matplotlib import cm
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx

import numpy as np
from numpy.random import uniform, seed
from scipy.interpolate import griddata

import xrayutilities as xu

import os

class MplCanvasFrame(wx.Frame):
    def __init__(self):
        #directory from which to read a file
        self.dirname = ''
        
        wx.Frame.__init__(self, None, wx.ID_ANY, size=(600, 400), title='Matplotlib Figure with Navigation Toolbar')
        
        #setting up a status bar in the bottom of the window
        self.CreateStatusBar()
        
        #setting up menu
        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "Open a file to edit")
        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", "Terminate the program")
        
        helpmenu = wx.Menu()
        menuAbout = helpmenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        
        #creating the menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        menuBar.Append(helpmenu, "&Help")
        
        self.SetMenuBar(menuBar) # Adding the MenuBar to the Frame content
        
        
        #Events
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        
        #creates SplitterWindow object within the wxFrame containing a panel on top and bottom
        self.sp = wx.SplitterWindow(self)
        
        self.mplPanel = MplPanel(self.sp)
        self.stgPanel = wx.Panel(self.sp, style = wx.SUNKEN_BORDER)
        
        self.sp.SplitVertically(self.mplPanel, self.stgPanel, 500)

    
    def OnOpen(self, evt):
        """Open a file"""
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.xrdml", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            
            self.SetStatusText(self.filename)
        dlg.Destroy()
        
        self.om,self.tt,self.psd = xu.io.getxrdml_map(self.dirname + os.sep + self.filename)
        gridder = xu.Gridder2D(150,150)
        gridder(self.om,self.tt, self.psd)
        INT = xu.maplog(gridder.data.transpose(),6,0)

        #clear axes from previous drawing
        self.mplPanel.figure.clf()
        #add subplot to the figure
        self.mplPanel.axes = self.mplPanel.figure.add_subplot(111)
        cf = self.mplPanel.axes.contourf(gridder.xaxis, gridder.yaxis,INT,100,extend='min')
        self.mplPanel.figure.colorbar(cf, ax = self.mplPanel.axes) # draw colorbar
        self.mplPanel.figure.canvas.draw()
        
    def OnExit(self, evt):
        self.Close(True)
    
    def OnAbout(self, evt):
        #Create a message dialog box
        dlg = wx.MessageDialog(self, "VXRD v0.21", "Reciprocal space map analyzer", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

class MplPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, size = (50, 50))
        # matplotlib figure
        self.figure = Figure()
        # initialize the FigureCanvas, mapping the figure to the WxAgg backend
        self.canvas = FigureCanvas(self, wx.ID_ANY, self.figure)
        # Box sizer for layout
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.EXPAND)
        
        # Navigation Toolbar
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        #needed to support Windows systems
        self.toolbar.Realize()
        # add it to the sizer
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        # show toolbar
        self.toolbar.Show()
        
        # sets the window to have the given layout sizer
        self.SetSizer(self.sizer)
        self.Fit()

class StgPanel(wx.Panel):
    pass
        
class MplApp(wx.App):
    def OnInit(self):
        #instantiate custom wxFrame 
        frame = MplCanvasFrame()
        #set it at the top-level window
        self.SetTopWindow(frame)
        # show it
        frame.Show(True)
        #return True to continue processing
        return True

#our wxApp class
mplapp = MplApp(False)
#start the loop
mplapp.MainLoop()
