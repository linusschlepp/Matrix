from tkinter import *
from tkinter.ttk import Combobox
from matrix_calculations import *
import matrix_operations as mp
from gui_output import WindowOutput


class Window:

    def __init__(self, win):

        self.win = win
        lbl_rows = Label(win, text='Insert rows', fg='red', font=('Helvetica', 8))
        lbl_rows.place(x=10, y=50)
        lbl_col = Label(win, text='Insert columns', fg='red', font=('Helvetica', 8))
        lbl_col.place(x=10, y=70)

        self.label_warning = None
        self.cb_row = Combobox(win, values=(2, 3, 4, 5, 6, 7, 8, 9))
        self.cb_col = Combobox(win, values=(2, 3, 4, 5, 6, 7, 8, 9))
        self.cb_row.current(1)
        self.cb_col.current(1)
        self.t1 = Entry()
        self.t2 = Entry()
        self.cb_row.place(x=70, y=50)
        self.cb_col.place(x=70, y=70)
        self.matrix_list_1 = []
        self.vector_list = []
        self.matrix_list_2 = []
        self.entries_1 = []
        self.entries_2 = []
        self.operation = None
        self.t3 = Text(win, height=50, width=130)
        self.t3.place(x=750, y=5)

        # Matrix gets solved
        self.btn_solve = Button(win, text='Solve', fg='blue',
                                command=lambda: self.convert_to_list_single(self.matrix_list_1, self.vector_list))
        # Grid is filled with random values
        self.btn_ran = Button(win, text='Fill with random values', fg='blue',
                              command=lambda: self.input_single_matrix(int(self.cb_row.get()), int(self.cb_col.get()),
                                                                       True))
        #
        self.btn_two = Button(win, text='Enter two Matrices', fg='blue',
                              command=lambda: self.input_two_matrix(int(self.cb_row.get()), int(self.cb_col.get()),
                                                                    False, False))

        self.btn_add = Button()
        self.btn_multiply = Button()
        self.btn_single = Button()

        self.btn_solve.place(x=20, y=100)
        self.btn_ran.place(x=75, y=100)
        self.btn_two.place(x=215, y=100)

        self.cb_col.bind("<<ComboboxSelected>>",
                         lambda x: self.input_single_matrix(int(self.cb_row.get()), int(self.cb_col.get()), False))
        self.cb_row.bind("<<ComboboxSelected>>",
                         lambda x: self.input_single_matrix(int(self.cb_row.get()), int(self.cb_col.get()), False))
        window.title('Matrix solver')
        window.geometry('1700x800+10+10')
        self.input_single_matrix(int(self.cb_row.get()), int(self.cb_col.get()), False)
        window.mainloop()

    def input_single_matrix(self, am_rows, am_cols, is_ran):

        if not self.label_warning is None:
            self.destroy_label_warning()

        self.btn_add.destroy()
        self.btn_multiply.destroy()
        self.btn_single.destroy()

        if not len(self.entries_2) == 0:
            self.input_two_matrix(am_rows, am_cols, False, is_ran)
            return

        # Clears the grid of the matrix, if it already exists
        if not len(self.entries_1) == 0 or not len(self.entries_2) == 0:
            # all entry-fields are removed from the layout
            for e in self.entries_1:
                e.destroy()
            for e in self.entries_2:
                e.destroy()
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

    def clear_second_matrix(self):

        if not self.label_warning is None:
            self.destroy_label_warning()

        for e in self.entries_2:
            e.destroy()
        self.entries_2.clear()

        self.btn_single.destroy()
        self.btn_multiply.destroy()
        self.btn_add.destroy()
        # Button to enter two matrices is being recreated
        self.btn_two = Button(self.win, text='Enter two Matrices', fg='blue',
                              command=lambda: self.input_two_matrix(int(self.cb_row.get()), int(self.cb_col.get()),
                                                                    False, False))
        # Solve Button is being recreated
        self.btn_solve = Button(self.win, text='Solve', fg='blue',
                                command=lambda: self.convert_to_list_single(self.matrix_list_1, self.vector_list))

        # Buttons are being placed
        self.btn_two.place(x=215, y=100)
        self.btn_solve.place(x=20, y=100)

    def input_two_matrix(self, am_rows, am_cols, multiply, is_ran):

        if not self.label_warning is None:
            self.destroy_label_warning()

        self.btn_two.destroy()
        self.btn_solve.destroy()

        # TODO: Find better and sleeker solution
        # TODO: Basically, refactor the whole code
        self.btn_add = Button(self.win, text='Add Matrices', fg='blue',
                              command=lambda: self.convert_to_list_double(self.matrix_list_1, self.matrix_list_2,
                                                                          False))
        self.btn_multiply = Button(self.win, text='Multiply Matrices', fg='blue',
                                   command=lambda: self.convert_to_list_double(self.matrix_list_1, self.matrix_list_2,
                                                                               True))
        self.btn_single = Button(self.win, text='Enter single Matrix', fg='blue',
                                 command=lambda: self.clear_second_matrix())
        # self.btn_add.pack()
        # self.btn_multiply.pack()
        # self.btn_single.pack()
        self.btn_add.place(x=380, y=100)
        self.btn_multiply.place(x=480, y=100)
        self.btn_single.place(x=620, y=100)

        if not len(self.entries_1) == 0:
            for e in self.entries_1:
                e.destroy()
            for e in self.entries_2:
                e.destroy()
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
    def convert_to_list_double(self, list_matrix_1, list_matrix_2, multiply):
        if not self.label_warning is None:
            self.destroy_label_warning()

        matrix_1 = [[0 for x in range(int(self.cb_col.get()))] for y in range(int(self.cb_row.get()))]
        matrix_2 = [[0 for x in range(int(self.cb_col.get()))] for y in range(int(self.cb_row.get()))]

        # TODO: Requires error handling as well
        try:
            index = 0
            for x in range(int(self.cb_row.get())):
                for y in range(int(self.cb_col.get())):
                    matrix_1[x][y] = float(list_matrix_1[index].get())
                    matrix_2[x][y] = float(list_matrix_2[index].get())
                    index = index + 1

            if multiply:
                mp.multiply_matrices(matrix_1, matrix_2)
            else:
                mp.add_matrices(matrix_1, matrix_2)
            # string_list gets inserted into the textarea
            self.t3.delete(1.0, END)
            self.t3.insert(1.0, mp.string_list)
        except ValueError:
            self.label_warning = Label(self.win, text="Enter values first!", fg="red")
            self.label_warning.place(x=30, y=350)

    # converts the grid, into the matrix and vector list
    def convert_to_list_single(self, list_matrix, list_vector):
        # self.destroy_label_warning()

        matrix = [[0 for x in range(int(self.cb_col.get()))] for y in range(int(self.cb_row.get()))]
        vector = []

        # TODO: IndexError gets thrown if dimension of columns and rows differ, this still needs to be fixed
        try:
            index = 0
            for x in range(int(self.cb_row.get())):
                for y in range(int(self.cb_col.get())):
                    matrix[x][y] = float(list_matrix[index].get())
                    index = index + 1
                vector.append(float(list_vector[x].get()))
            solve_matrix(matrix, vector)
            self.t3.delete(1.0, END)
            self.t3.insert(1.0, string_list)
            print_list()
        except ValueError:
            # TODO: Make label disappear
            self.label_warning = Label(self.win, text="Enter values first!", fg="red")
            self.label_warning.place(x=30, y=350)

    def destroy_label_warning(self):
        self.label_warning.destroy()

    # WindowOutput()


window = Tk()
mywin = Window(window)
