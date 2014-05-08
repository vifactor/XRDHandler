# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.4 on Thu May  8 16:52:44 2014

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade


class PreferencesDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PreferencesDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.label_2 = wx.StaticText(self, -1, "Figure")
        self.lbWidth = wx.StaticText(self, -1, "Width")
        self.tcWidth = wx.TextCtrl(self, -1, "")
        self.lbHeight = wx.StaticText(self, -1, "Height")
        self.tcHeight = wx.TextCtrl(self, -1, "")
        self.lbDPI = wx.StaticText(self, -1, "dpi")
        self.tcDPI = wx.TextCtrl(self, -1, "")
        self.lbAxesRatio = wx.StaticText(self, -1, "Axes ratio")
        self.tcAxesRatio = wx.TextCtrl(self, -1, "")
        self.bCancel = wx.Button(self, wx.ID_CANCEL, "Cancel")
        self.bOK = wx.Button(self, wx.ID_CANCEL, "OK")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: PreferencesDialog.__set_properties
        self.SetTitle("Preferences")
        self.label_2.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PreferencesDialog.__do_layout
        sizer_18 = wx.BoxSizer(wx.VERTICAL)
        sizer_19 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_20 = wx.BoxSizer(wx.VERTICAL)
        sizer_31 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_21 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_20.Add(self.label_2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_21.Add(self.lbWidth, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_21.Add(self.tcWidth, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_21.Add(self.lbHeight, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_21.Add(self.tcHeight, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_21.Add(self.lbDPI, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_21.Add(self.tcDPI, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_20.Add(sizer_21, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 10)
        sizer_31.Add(self.lbAxesRatio, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_31.Add(self.tcAxesRatio, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_20.Add(sizer_31, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_18.Add(sizer_20, 0, wx.EXPAND, 0)
        sizer_19.Add(self.bCancel, 0, 0, 0)
        sizer_19.Add(self.bOK, 0, 0, 0)
        sizer_18.Add(sizer_19, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        self.SetSizer(sizer_18)
        sizer_18.Fit(self)
        self.Layout()
        # end wxGlade

# end of class PreferencesDialog