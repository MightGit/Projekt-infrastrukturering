from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from sympy.parsing.sympy_parser import parse_expr
import sympy as sym


class mainWindow:

    def __init__(self):

        y1=200
        x0=50
        x1=100
        self.root = Tk()

        velkomst = Label(self.root, text="Graf udregner")
        velkomst.pack(pady=10)


        self.fx = Entry(self.root)
        self.fx.pack()
        if len(self.fx.get()) == 0:
            self.fx.insert(END, 'indsæt funktion')


        self.x0 = Entry(self.root)
        self.x0.pack()
        if len(self.x0.get()) == 0:
            self.x0.insert(END, 'indsæt din x0 her')

        self.x1 = Entry(self.root)
        self.x1.pack()
        if len(self.x1.get()) == 0:
            self.x1.insert(END, 'indsæt din x1 her')

        def getFunctionFromString(inputString='y= x**2'):

            # Tjek efter om brugeren har tastet = ind i.

            if '=' in inputString:
                user_input = inputString.split('=')[1]  # Del input strengen op ved '=', og giv anden del tilbage.
            else:
                user_input = inputString

            print(f'This is the mathematical function we are about to make into a real python funktion: {user_input}')

            x, y = sym.symbols('x y')

            expr = parse_expr(user_input)

            f = sym.lambdify([x], expr)

            return f

        def plot():
            fig, ax = plt.subplots()

            f = getFunctionFromString(self.fx.get())
            try:
                x0=int(self.x0.get())
            except:
                x0 = 0
            try:
                x1=int(self.x1.get())
            except:
                x1 = 100
            X=np.arange(x0,x1,0.1)
            Y=f(X)
            ax.plot(X,Y)
            ax.set_title(f'Plot af funktionen: {self.fx.get()}')
            ax.set_xlabel('X - Akse')
            ax.set_ylabel('Y - Akse')
            plt.show()


        pltBtn = Button(self.root,text ="plotwin",command = plot)
        pltBtn.pack(padx = 20, pady = 10,side=LEFT)

        # infinite loop
        mainloop()

        #det her kører når man trykker luk:
        #afslut()



if __name__ == '__main__':
    main = mainWindow()
