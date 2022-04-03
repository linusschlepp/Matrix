import random
from tkinter import *
from tkinter.ttk import Combobox
import matrix_calculations as mcal
import matrix_operations as mp
import operations as op
import numpy



class Window:
    def __init__(self, win):

        self.win = win
        # icon for the application is getting added
        # self.win.iconphoto(False, ImageTk.PhotoImage(file='images/appIcon.ico'))
        self.win.iconbitmap(r'C:\Users\linus\PycharmProjects\Matrix\images\appIcon.ico')
        lbl_rows = Label(win, text='Insert rows', fg='red', font=('Helvetica', 8))
        lbl_col = Label(win, text='Insert columns', fg='red', font=('Helvetica', 8))
        self.lbl_matrix_1 = Label(win, text='Matrix 1:', fg='black', font=('Helvetica', 10, 'bold italic'))
        self.lbl_matrix_2 = Label()
        self.lbl_warning = Label()
        self.cb_row = Combobox(win, values=(2, 3, 4, 5, 6, 7, 8, 9))
        self.cb_col = Combobox(win, values=(2, 3, 4, 5, 6, 7, 8, 9))
        self.cb_row.current(1)
        self.cb_col.current(1)
        self.t1 = Entry()
        self.t2 = Entry()
        self.matrix_list_1 = []
        self.vector_list = []
        self.matrix_list_2 = []
        self.entries_1 = []
        self.entries_2 = []
        self.t3 = Text(win, height=50, width=130)
        self.btn_add = Button()
        self.btn_subtract = Button()
        self.btn_multiply = Button()
        self.btn_single = Button()

        # Matrix gets solved
        self.btn_solve = Button(win, text='Solve', fg='blue',
                                command=lambda: self.convert_to_list_single(self.matrix_list_1, self.vector_list))
        # Grid is filled with random values
        self.btn_ran = Button(win, text='Fill with random values', fg='blue',
                              command=lambda: self.input_single_matrix(int(self.cb_row.get()), int(self.cb_col.get()),
                                                                       True))
        # Enables the input of two matrices
        self.btn_two = Button(win, text='Enter two Matrices', fg='blue',
                              command=lambda: self.input_two_matrix(int(self.cb_row.get()), int(self.cb_col.get()),
                                                                    False))

        # Bind function to comboBox
        self.cb_col.bind("<<ComboboxSelected>>",
                         lambda x: self.input_single_matrix(int(self.cb_row.get()), int(self.cb_col.get()), False))

        # Bind function to comboBox
        self.cb_row.bind("<<ComboboxSelected>>",
                         lambda x: self.input_single_matrix(int(self.cb_row.get()), int(self.cb_col.get()), False))

        self.btn_solve.place(x=20, y=100)
        self.btn_ran.place(x=75, y=100)
        self.btn_two.place(x=215, y=100)
        self.t3.place(x=840, y=5)
        self.cb_row.place(x=90, y=50)
        self.cb_col.place(x=90, y=70)
        self.lbl_matrix_1.place(x=30, y=140)
        lbl_col.place(x=10, y=70)
        lbl_rows.place(x=10, y=50)

        window.title('Matrix solver')
        window.geometry('1700x800+10+10')
        self.input_single_matrix(int(self.cb_row.get()), int(self.cb_col.get()), False)
        window.mainloop()

    def input_single_matrix(self, am_rows, am_cols, is_ran):

        self.btn_add.destroy()
        self.btn_multiply.destroy()
        self.btn_single.destroy()
        self.btn_subtract.destroy()
        self.lbl_warning.destroy()
        self.lbl_matrix_2.destroy()

        if not len(self.entries_2) == 0:
            self.input_two_matrix(am_rows, am_cols, is_ran)
            return

        # Clears the grid of the matrix, if it already exists
        if not len(self.entries_1) == 0 or not len(self.entries_2) == 0:
            # all entry-fields are removed from the layout
            [e.destroy() for e in self.entries_1]
            [e.destroy() for e in self.entries_2]

            # The lists get cleared as well:
            self.matrix_list_1.clear()
            self.vector_list.clear()
            self.matrix_list_2.clear()
            self.vector_list.clear()

        # Creates the grid of the matrix
        for row in range(am_rows):
            for col in range(am_cols + 1):
                self.t1 = Entry(width=5)
                self.t1.place(x=10 + (col + 1) * 20, y=150 + (row + 1) * 20)
                # if is_ran is True a random matrix and vector is getting created
                if is_ran:
                    self.t1.insert(0, int(random.randint(0, 20)))
                self.entries_1.append(self.t1)
                if col < am_cols:
                    self.matrix_list_1.append(self.t1)
                else:
                    self.vector_list.append(self.t1)

    # second grid is cleared
    def clear_second_matrix(self):
        # grid 2 is getting destroyed/ all entry fields are removed from the layout
        [e.destroy() for e in self.entries_2]

        # all itmes within the list of entries_2 are deleted
        self.entries_2.clear()
        self.lbl_warning.destroy()
        self.btn_single.destroy()
        self.btn_multiply.destroy()
        self.btn_add.destroy()
        self.btn_subtract.destroy()
        self.lbl_matrix_2.destroy()

        # Button to enter two matrices is being recreated
        self.btn_two = Button(self.win, text='Enter two Matrices', fg='blue',
                              command=lambda: self.input_two_matrix(int(self.cb_row.get()), int(self.cb_col.get()),
                                                                    False))
        # Solve Button is being recreated
        self.btn_solve = Button(self.win, text='Solve', fg='blue',
                                command=lambda: self.convert_to_list_single(self.matrix_list_1, self.vector_list))

        # Buttons are being placed
        self.btn_two.place(x=215, y=100)
        self.btn_solve.place(x=20, y=100)
        self.input_single_matrix(int(self.cb_row.get()), int(self.cb_col.get()), False)

    def input_two_matrix(self, am_rows, am_cols, is_ran):

        self.btn_two.destroy()
        self.btn_solve.destroy()
        self.lbl_warning.destroy()

        # Buttons are created
        self.btn_add = Button(self.win, text='Add Matrices', fg='blue',
                              command=lambda: self.convert_to_list_double(self.matrix_list_1, self.matrix_list_2,
                                                                          op.Operation.ADD))
        self.btn_subtract = Button(self.win, text='Subtract Matrices', fg='blue',
                                   command=lambda: self.convert_to_list_double(self.matrix_list_1, self.matrix_list_2,
                                                                               op.Operation.SUBTRACT))
        self.btn_multiply = Button(self.win, text='Multiply Matrices', fg='blue',
                                   command=lambda: self.convert_to_list_double(self.matrix_list_1, self.matrix_list_2,
                                                                               op.Operation.MULTIPLY))
        self.btn_single = Button(self.win, text='Enter single Matrix', fg='blue',
                                 command=lambda: self.clear_second_matrix())

        self.lbl_matrix_2 = Label(self.win, text='Matrix 2:', fg='black', font=('Helvetica', 10, 'bold italic'))

        # After the buttons were created, they are placed
        self.btn_add.place(x=380, y=100)
        self.btn_multiply.place(x=480, y=100)
        self.btn_subtract.place(x=600, y=100)
        self.btn_single.place(x=720, y=100)
        self.lbl_matrix_2.place(x=230, y=140)

        if not len(self.entries_1) == 0:
            [e.destroy() for e in self.entries_1]
            [e.destroy() for e in self.entries_2]
        # The lists get cleared as well:
        self.matrix_list_1.clear()
        self.vector_list.clear()
        self.matrix_list_2.clear()
        self.vector_list.clear()

        for row in range(am_rows):
            for col in range(am_cols):
                self.t1 = Entry(width=5)
                self.t2 = Entry(width=5)
                self.t1.place(x=10 + (col + 1) * 20, y=150 + (row + 1) * 20)
                self.t2.place(x=210 + (col + 1) * 20, y=150 + (row + 1) * 20)
                # if is_ran is True a random matrix and vector is getting created
                if is_ran:
                    self.t1.insert(0, int(random.randint(0, 20)))
                    self.t2.insert(0, int(random.randint(0, 20)))
                self.entries_1.append(self.t1)
                self.entries_2.append(self.t2)
                self.matrix_list_1.append(self.t1)
                self.matrix_list_2.append(self.t2)

    # converts two matrices into arrays, to perform calculations on them
    def convert_to_list_double(self, list_matrix_1, list_matrix_2, operation):

        self.lbl_warning.destroy()
        matrix_1 = [[0 for x in range(int(self.cb_col.get()))] for y in range(int(self.cb_row.get()))]
        matrix_2 = [[0 for x in range(int(self.cb_col.get()))] for y in range(int(self.cb_row.get()))]

        try:
            index = 0
            for x in range(int(self.cb_row.get())):
                for y in range(int(self.cb_col.get())):
                    matrix_1[x][y] = float(list_matrix_1[index].get())
                    matrix_2[x][y] = float(list_matrix_2[index].get())
                    index = index + 1

            if operation == op.Operation.MULTIPLY:
                mp.multiply_matrices(matrix_1, matrix_2)
            elif operation == op.Operation.ADD:
                mp.add_matrices(matrix_1, matrix_2)
            else:
                mp.subtract_matrices(matrix_1, matrix_2)
            # string_list gets inserted into the textarea
            self.t3.delete(1.0, END)
            self.t3.insert(1.0, mp.string_list)
        # ValueError gets thrown if no values have been entered, to counter that error lbl_warning is getting displayed
        except ValueError:
            self.lbl_warning = Label(self.win, text="Enter values first!", fg="red")
            self.lbl_warning.place(x=30, y=350)

    # converts the grid, into the matrix and vector list
    def convert_to_list_single(self, list_matrix, list_vector):

        matrix = [[0 for x in range(int(self.cb_col.get()))] for y in range(int(self.cb_row.get()))]
        vector = []
        try:
            index = 0
            for x in range(int(self.cb_row.get())):
                for y in range(int(self.cb_col.get())):
                    matrix[x][y] = float(list_matrix[index].get())
                    index = index + 1
                vector.append(float(list_vector[x].get()))
            # after the grids have been converted to a list they are passed to the function solve_matrix in
            # matrix_calculations.py
            mcal.solve_matrix(matrix, vector)
            self.t3.delete(1.0, END)
            self.t3.insert(1.0, mcal.string_list)
        except ValueError:
            self.lbl_warning = Label(self.win, text="Enter values first!", fg="red")
            self.lbl_warning.place(x=30, y=350)


window = Tk()
mywin = Window(window)
