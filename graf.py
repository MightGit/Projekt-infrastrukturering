from tkinter import *
from tkinter.ttk import * #progressbar
from plotter import PlotterClass
class mainWindow:

    def __init__(self):

        self.root = Tk()

        velkomst = Label(self.root, text="Velkommen til GUI")
        velkomst.pack(pady=10)

        # Progress bar widget
        listButton = Button(self.root,text ="tryk",command = self.test)
        listButton.pack(padx = 20, pady = 10,side=LEFT)


        pltBtn = Button(self.root,text ="plotwin",command = lambda: PlotterClass(self))
        pltBtn.pack(padx = 20, pady = 10,side=LEFT)

        # infinite loop
        mainloop()

        #det her kører når man trykker luk:
        #afslut()
    def test(self):
        pass

if __name__ == '__main__':
    main = mainWindow()
