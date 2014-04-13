# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.4 on Sun Apr 13 19:15:26 2014

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade


class StgPanel(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: StgPanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.viewMode = wx.ComboBox(self, -1, choices=["Angles", "Reciprocal points"], style=wx.CB_DROPDOWN | wx.CB_READONLY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.OnViewModeSelect, self.viewMode)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: StgPanel.__set_properties
        self.viewMode.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: StgPanel.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_3.Add(self.viewMode, 0, 0, 0)
        self.SetSizer(sizer_3)
        sizer_3.Fit(self)
        # end wxGlade

    def OnViewModeSelect(self, event):  # wxGlade: StgPanel.<event_handler>
        sp = self.GetParent()
        frame = sp.GetParent()
        
        print self.viewMode.GetSelection()
        print self.viewMode.GetCurrentSelection()
        print "Event handler `OnViewModeSelect' not implemented"
        event.Skip()

# end of class StgPanel