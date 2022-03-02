from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from sympy.parsing.sympy_parser import parse_expr
import sympy as sym

class PlotterClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.plotwin = Toplevel(self.master.root)

