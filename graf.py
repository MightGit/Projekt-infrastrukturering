from tkinter import *
from tkinter.ttk import * #progressbar
from plotter import PlotterClass
import numpy as np
import matplotlib.pyplot as plt

class mainWindow:

    def __init__(self):

        y1=200
        x0=50
        x1=100
        self.root = Tk()

        velkomst = Label(self.root, text="Velkommen til GUI")
        velkomst.pack(pady=10)

        self.x0 = Entry(self.root)
        self.x0.pack()
        if len(self.x0.get()) == 0:
            self.x0.insert(END, 'indsæt din x0 her')

        self.x1 = Entry(self.root)
        self.x1.pack()
        if len(self.x1.get()) == 0:
            self.x1.insert(END, 'indsæt din x1 her')


        def f(x0,x1):
            graph=np.random.normal(x0,x1,y1)
            plt.hist(graph,50)
            plt.show()


        pltBtn = Button(self.root,text ="plotwin",command = f(x0,x1))
        pltBtn.pack(padx = 20, pady = 10,side=LEFT)

        # infinite loop
        mainloop()

        #det her kører når man trykker luk:
        #afslut()



if __name__ == '__main__':
    main = mainWindow()
