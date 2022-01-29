from tkinter import *
from tkinter.ttk import Combobox
from matrix_calculations import *


class Window:

    def __init__(self, win):

        lbl_rows = Label(win, text='Insert rows', fg='red', font=('Helvetica', 8))
        lbl_rows.place(x=10, y=50)
        lbl_col = Label(win, text='Insert columns', fg='red', font=('Helvetica', 8))
        lbl_col.place(x=10, y=70)

        self.cb_row = Combobox(win, values=(2, 3, 4, 5, 6, 7, 8, 9))
        self.cb_col = Combobox(win, values=(2, 3, 4, 5, 6, 7, 8, 9))
        self.cb_row.current(1)
        self.cb_col.current(1)
        self.cb_row.place(x=70, y=50)
        self.cb_col.place(x=70, y=70)
        self.matrix_list = []
        self.vector_list = []
        btn = Button(win, text='Solve Matrix', fg='blue', command =lambda: self.print_list(self.matrix_list, self.vector_list))
        btn.place(x=80, y=100)
        self.cb_col.bind("<<ComboboxSelected>>", lambda x: self.show_matrix(int(self.cb_row.get()), int(self.cb_col.get())))
        self.cb_row.bind("<<ComboboxSelected>>", lambda x: self.show_matrix(int(self.cb_row.get()), int(self.cb_col.get())))
        window.title('Matrix solver')
        window.geometry('700x700+10+10')
        window.mainloop()

    def show_matrix(self, am_rows, am_cols):

        for row in range(am_rows):
            for col in range(am_cols + 1):
                self.t1 = Entry(width=5)
                self.t1.place(x=10 + (col + 1) * 20, y=150 + (row + 1) * 20)
                if col < am_cols:
                    self.matrix_list.append(self.t1)
                else:
                    self.vector_list.append(self.t1)

    def print_list(self, list_matrix, list_vector):

        matrix = [[0 for x in range(int(self.cb_row.get()))] for y in range(int(self.cb_col.get()))]
        vector = []


        index = 0
        for x in range(int(self.cb_row.get())):
            for y in range(int(self.cb_col.get())):
                matrix[x][y] = float(list_matrix[index].get())
                index = index+1
            vector.append(float(list_vector[x].get()))

        solve_matrix(matrix, vector)
        print_list()



window = Tk()
mywin = Window(window)
