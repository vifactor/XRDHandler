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
        
        #Dummy DataReader
        dr = DataReader("test.txt")
        
        # Map Data Handler
        mdh = MapGridder(sampling = 60, method = 'cubic', fill_value = 0)
        mdh.setup(dr.get_points())
        xg, yg, zg = mdh.get_map()
        
        # matplotlib figure
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        # contour the gridded data, plotting dots at the randomly spaced data points.
        self.axes.contour(xg,yg,zg,15,linewidths=0.5,colors='k')
        cs = self.axes.contourf(xg,yg,zg,15, cmap=cm.jet)
        self.figure.colorbar(cs) # draw colorbar
        # plot data points.
        #self.axes.scatter(x, y, marker='o',c='b',s=5)
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
    
    def OnOpen(self, evt):
        """Open a file"""
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            
            self.SetStatusText(self.filename)
        dlg.Destroy()
    
    def OnExit(self, evt):
        self.Close(True)
    
    def OnAbout(self, evt):
        #Create a message dialog box
        dlg = wx.MessageDialog(self, "VXRD v0.1", "Reciprocal space map analyzer", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
        
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

class DataReader:
    def __init__(self, filename):
        self.points = []
        
        #temporary solution
        npts = 50
        x = uniform(-2,2,npts)
        y = uniform(-2,2,npts)
        z = x**2 * np.exp(-x**2-y**2)
        for i in range(npts):
            self.points.append([x[i], y[i], z[i]])
        
        
    def get_points(self):
        return self.points

class MapGridder:
    def __init__(self, sampling, method, fill_value):
        self.raw_x = []
        self.raw_y = []
        self.raw_z = []
        
        self.xl = None
        self.xu = None
        self.yl = None
        self.yu = None
        
        self.sampling = sampling
        self.grid_method = method
        self.fill_value = fill_value
        
    def setup(self, points):
        self.raw_x = []
        self.raw_y = []
        self.raw_z = []

        for point in points:
            self.raw_x.append(point[0])
            self.raw_y.append(point[1])
            self.raw_z.append(point[2])
            
        self.xl = min(self.raw_x)
        self.xu = max(self.raw_x)
        self.yl = min(self.raw_y)
        self.yu = max(self.raw_y)
            
    def set_xlim(self, xl, xu):
        self.xl = xl
        self.xu = xu
        
    def set_ylim(self, yl, yu):
        self.yl = yl
        self.yu = yu
        
    def get_map(self):
        x = np.linspace(self.xl, self.xu, self.sampling)
        y = np.linspace(self.yl, self.yu, self.sampling)
        
        #Prepare the gridded map
        z = griddata((self.raw_x, self.raw_y), self.raw_z, (x[None,:], y[:,None]), method = self.grid_method, fill_value = self.fill_value )
        # The following is not strictly essential, but it will eliminate
        # a warning.  Comment it out to see the warning.
        #z = np.ma.masked_where(z<=0, z)
        
        return (x, y, z)


#our wxApp class
mplapp = MplApp(False)
#start the loop
mplapp.MainLoop()
