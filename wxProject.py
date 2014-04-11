import wx

from matplotlib import cm
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx

import numpy as np
from numpy.random import uniform, seed
from scipy.interpolate import griddata

class MplCanvasFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, size=(600, 400), title='Matplotlib Figure with Navigation Toolbar')
        # make up some randomly distributed data
        seed(1234)
        npts = 200
        x = uniform(-2,2,npts)
        y = uniform(-2,2,npts)
        z = x*np.exp(-x**2-y**2)
        # define grid.
        xi = np.linspace(-2.1,2.1,100)
        yi = np.linspace(-2.1,2.1,100)
        # grid the data.
        zi = griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')

        # matplotlib figure
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        # contour the gridded data, plotting dots at the randomly spaced data points.
        self.axes.contour(xi,yi,zi,15,linewidths=0.5,colors='k')
        cs = self.axes.contourf(xi,yi,zi,15, cmap=cm.jet)
        self.figure.colorbar(cs) # draw colorbar
        # plot data points.
        self.axes.scatter(x,y,marker='o',c='b',s=5)
        self.axes.set_xlim(-2,2)
        self.axes.set_ylim(-2,2)
        
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
