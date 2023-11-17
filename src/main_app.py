# src/main_app/py
# @dev this is the main app where the gui is called and the application is initialised 


import wx
from gui.main_window import main_window

class MyApp(wx.App):
    def OnInit(self):
        self.frame = main_window(None, title="MySQL DB App")
        self.SetTopWindow(self.frame)
        return True

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
