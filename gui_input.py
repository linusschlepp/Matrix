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
        self.t3 = Text(win, height=50, width=100)
        self.t3.place(x=750, y=5)

        self.btn_solve = Button(win, text='Solve', fg='blue',
                                command=lambda: self.convert_to_list_single(self.matrix_list_1, self.vector_list))
        self.btn_ran = Button(win, text='Fill with random values', fg='blue',
                              command=lambda: self.show_matrix(int(self.cb_row.get()), int(self.cb_col.get()), True))
        self.btn_two = Button(win, text='Enter two Matrices', fg='blue',
                              command=lambda: self.matrix_operations(int(self.cb_row.get()), int(self.cb_col.get()),
                                                                     False, False))

        self.btn_add = Button()
        self.btn_multiply = Button()
        self.btn_single = Button()

        self.btn_solve.place(x=20, y=100)
        self.btn_ran.place(x=75, y=100)
        self.btn_two.place(x=215, y=100)

        self.cb_col.bind("<<ComboboxSelected>>",
                         lambda x: self.show_matrix(int(self.cb_row.get()), int(self.cb_col.get()), False))
        self.cb_row.bind("<<ComboboxSelected>>",
                         lambda x: self.show_matrix(int(self.cb_row.get()), int(self.cb_col.get()), False))
        window.title('Matrix solver')
        window.geometry('1500x700+10+10')
        self.show_matrix(int(self.cb_row.get()), int(self.cb_col.get()), False)
        window.mainloop()

    def show_matrix(self, am_rows, am_cols, is_ran):

        self.btn_add.pack_forget()
        self.btn_multiply.pack_forget()
        self.btn_single.pack_forget()

        if not len(self.entries_2) == 0:
            self.matrix_operations(am_rows, am_cols, False, is_ran)
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
        for e in self.entries_2:
            e.destroy()
        self.entries_2.clear()

        self.btn_single.destroy()
        self.btn_multiply.destroy()
        self.btn_add.destroy()
        self.btn_two = Button(self.win, text='Enter two Matrices', fg='blue',
                              command=lambda: self.matrix_operations(int(self.cb_row.get()), int(self.cb_col.get()),
                                                                     False, False))

        self.btn_two.place(x=215, y=100)

    def matrix_operations(self, am_rows, am_cols, multiply, is_ran):

        self.btn_two.destroy()

        # TODO: Still need to find the right commands for both buttons
        self.btn_add = Button(self.win, text='Add Matrices', fg='blue',
                              command=lambda: self.convert_to_list_double(self.matrix_list_1, self.matrix_list_2,
                                                                          False))
        self.btn_multiply = Button(self.win, text='Multiply Matrices', fg='blue',
                                   command=lambda: self.convert_to_list_double(self.matrix_list_1, self.matrix_list_2,
                                                                               True))
        self.btn_single = Button(self.win, text='Enter single Matrix', fg='blue',
                                 command=lambda: self.clear_second_matrix())
        self.btn_add.pack()
        self.btn_multiply.pack()
        self.btn_single.pack()
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

    def convert_to_list_double(self, list_matrix_1, list_matrix_2, multiply):
        matrix_1 = [[0 for x in range(int(self.cb_row.get()))] for y in range(int(self.cb_col.get()))]
        matrix_2 = [[0 for x in range(int(self.cb_row.get()))] for y in range(int(self.cb_col.get()))]

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

        self.t3.insert(1.0, mp.string_list)

    # converts the grid, into the matrix and vector list
    def convert_to_list_single(self, list_matrix, list_vector):

        matrix = [[0 for x in range(int(self.cb_row.get()))] for y in range(int(self.cb_col.get()))]
        vector = []
        # TODO: IndexError gets thrown if dimension of columns and rows differ, this still needs to be fixed
        index = 0
        for x in range(int(self.cb_row.get())):
            for y in range(int(self.cb_col.get())):
                matrix[x][y] = float(list_matrix[index].get())
                index = index + 1
            vector.append(float(list_vector[x].get()))

        solve_matrix(matrix, vector)
        print_list()
    # WindowOutput()


window = Tk()
mywin = Window(window)