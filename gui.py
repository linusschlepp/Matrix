from tkinter import *
from tkinter.ttk import Combobox
import pandas as pd


class Window:

    def __init__(self, win):

        lbl_rows = Label(win, text='Insert rows', fg='red', font=('Helvetica', 8))
        lbl_rows.place(x=10, y=50)
        lbl_col = Label(win, text='Insert columns', fg='red', font=('Helvetica', 8))
        lbl_col.place(x=10, y=70)

        cb_row = Combobox(win, values=(2, 3, 4, 5, 6, 7, 8, 9))
        cb_col = Combobox(win, values=(2, 3, 4, 5, 6, 7, 8, 9))
        cb_row.current(1)
        cb_col.current(1)
        cb_row.place(x=70, y=50)
        cb_col.place(x=70, y=70)
        matrix = [[0 for x in range(cb_row.current())] for y in range(cb_col.current() + 1)]
        vector = []
        btn = Button(win, text='Solve Matrix', fg='blue', command=print(pd.DataFrame(matrix)))
        btn.place(x=80, y=100)
        cb_col.bind("<<ComboboxSelected>>", lambda x: self.show_matrix(int(cb_row.get()), int(cb_col.get())))
        cb_row.bind("<<ComboboxSelected>>", lambda x: self.show_matrix(int(cb_row.get()), int(cb_col.get())))
        window.title('Matrix solver')
        window.geometry('700x700+10+10')
        window.mainloop()

    def show_matrix(self, am_rows, am_cols):

        self.matrix = [[0 for x in range(am_rows)] for y in range(am_cols)]
        self.vector = []

        for row in range(am_rows):
            for col in range(am_cols + 1):
                self.t1 = Entry(width=5)
                self.t1.place(x=10 + (col + 1) * 20, y=150 + (row + 1) * 20)
                if col < am_cols:
                    self.matrix[row][col] = self.t1.get()
                else:
                    self.vector.append(self.t1.get())


window = Tk()
mywin = Window(window)
