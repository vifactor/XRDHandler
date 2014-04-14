# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.4 on Sun Apr 13 19:15:26 2014

import wx

import xrayutilities as xu

import os

# begin wxGlade: dependencies
from StgPanel import StgPanel
from MplPanel import MplPanel
# end wxGlade

# begin wxGlade: extracode

# end wxGlade


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.MAXIMIZE | wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.RESIZE_BORDER | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        self.Open = wx.MenuItem(wxglade_tmp_menu, wx.ID_OPEN, "&Open", "Open a file to load", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.Open)
        self.Exit = wx.MenuItem(wxglade_tmp_menu, wx.ID_EXIT, "E&xit", "Terminate the program", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.Exit)
        self.menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()
        self.About = wx.MenuItem(wxglade_tmp_menu, wx.ID_ABOUT, "&About", "Information about this program", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.About)
        self.menubar.Append(wxglade_tmp_menu, "Help")
        self.SetMenuBar(self.menubar)
        # Menu Bar end
        self.statusbar = self.CreateStatusBar(1, 0)
        self.mplPanel = MplPanel(self, wx.ID_ANY)
        self.stgPanel = StgPanel(self, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.OnOpen, self.Open)
        self.Bind(wx.EVT_MENU, self.OnExit, self.Exit)
        self.Bind(wx.EVT_MENU, self.OnAbout, self.About)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle("RSM Handler")
        self.statusbar.SetStatusWidths([-1])
        # statusbar fields
        statusbar_fields = ["frame_1_statusbar"]
        for i in range(len(statusbar_fields)):
            self.statusbar.SetStatusText(statusbar_fields[i], i)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.mplPanel, 1, wx.ALL | wx.EXPAND, 5)
        sizer_1.Add(self.stgPanel, 0, wx.ALL, 5)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def OnOpen(self, event):  # wxGlade: MainFrame.<event_handler>
        """Open a file"""
        dlg = wx.FileDialog(self, "Choose a file", "", "", "*.xrdml", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            
            self.SetStatusText(self.filename)
        dlg.Destroy()
        
        self.om,self.tt,self.psd = xu.io.getxrdml_map(os.path.join(self.dirname + os.sep, self.filename))
        
        self.mplPanel.drawAngularMap(self.om,self.tt,self.psd)

    def OnExit(self, event):  # wxGlade: MainFrame.<event_handler>
        self.Close(True)

    def OnAbout(self, event):  # wxGlade: MainFrame.<event_handler>
        #Create a message dialog box
        dlg = wx.MessageDialog(self, "RSM Handler v0.4", "XRD", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        

# end of class MainFrame
