# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.4 on Sun Apr 13 19:15:26 2014

import wx

from matplotlib import cm
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx

import xrayutilities as xu

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade


class MplPanel(wx.Panel):
    def __init__(self, *args, **kwds):
        # matplotlib figure
        self.figure = Figure()
        
        # begin wxGlade: MplPanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.canvas = FigureCanvas(self, wx.ID_ANY, self.figure)
        self.toolbar = NavigationToolbar2Wx(self.canvas)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        
        #needed to support Windows systems
        self.toolbar.Realize()
        # show toolbar
        self.toolbar.Show()

    def __set_properties(self):
        # begin wxGlade: MplPanel.__set_properties
        pass
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MplPanel.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.canvas, 1, wx.EXPAND, 0)
        sizer_2.Add(self.toolbar, 0, 0, 0)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        # end wxGlade
    
    def drawAngularMap(self, om, tt, psd):
        gridder = xu.Gridder2D(150,150)
        gridder(om, tt, psd)
        INT = xu.maplog(gridder.data.transpose(),6,0)

        #clear axes from previous drawing
        self.figure.clf()
        #add subplot to the figure
        self.axes = self.figure.add_subplot(111)
        cf = self.axes.contourf(gridder.xaxis, gridder.yaxis,INT,100,extend='min')
        self.figure.colorbar(cf, ax = self.axes) # draw colorbar
        self.figure.canvas.draw()

    def drawReciprocalMap(self, om, tt, psd):
        pass

# end of class MplPanel
