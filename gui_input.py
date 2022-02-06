from tkinter import *
from tkinter.ttk import Combobox
from matrix_calculations import *
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
        self.btn_solve = Button(win, text='Solve Matrix', fg='blue',
                                command=lambda: self.convert_to_list(self.matrix_list_1, self.vector_list))
        self.btn_ran = Button(win, text='Fill with random values', fg='blue',
                              command=lambda: self.show_matrix(int(self.cb_row.get()), int(self.cb_col.get()), True))
        self.btn_two = Button(win, text='Enter two Matrices', fg='blue',
                              command=lambda: self.matrix_operations(int(self.cb_row.get()), int(self.cb_col.get()),
                                                                     False, False))

        self.btn_add = None
        self.btn_multiply = None


        self.btn_solve.place(x=10, y=100)
        self.btn_ran.place(x=95, y=100)
        self.btn_two.place(x=250, y=100)

        self.cb_col.bind("<<ComboboxSelected>>",
                         lambda x: self.show_matrix(int(self.cb_row.get()), int(self.cb_col.get()), False))
        self.cb_row.bind("<<ComboboxSelected>>",
                         lambda x: self.show_matrix(int(self.cb_row.get()), int(self.cb_col.get()), False))
        window.title('Matrix solver')
        window.geometry('700x700+10+10')
        window.mainloop()

    def show_matrix(self, am_rows, am_cols, is_ran):

        # TODO: Both Buttons need to disappear if possible
        if not self.btn_add == None and not self.btn_multiply == None:
            self.btn_add.destroy()
            self.btn_multiply.destroy()

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

    def matrix_operations(self, am_rows, am_cols, multiply, is_ran):

        #TODO: Still need to find the right commands for both buttons
        self.btn_add = Button(self.win, text='Add Matrices', fg='blue',
                              command=lambda: self.matrix_operations(int(self.cb_row.get()), int(self.cb_col.get()),
                                                                     True, False))
        self.btn_multiply = Button(self.win, text='Multiply Matrices', fg='blue',
                                   command=lambda: self.matrix_operations(int(self.cb_row.get()),
                                                                          int(self.cb_col.get()),
                                                                          True, False))
        self.btn_add.place(x=380, y=100)
        self.btn_multiply.place(x=480, y=100)

        if not len(self.entries_1) == 0:
            for e in self.entries_1:
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

    # converts the grid, into the matrix and vector list
    def convert_to_list(self, list_matrix, list_vector):

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
