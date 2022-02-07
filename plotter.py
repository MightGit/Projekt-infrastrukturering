from tkinter import *


class PlotterClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.plotwin = Toplevel(self.master.root)