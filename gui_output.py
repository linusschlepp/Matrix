from tkinter import *
import subprocess
from tkinter.ttk import Combobox
from matrix_calculations import *


class WindowOutput:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('900x700')

        self.proc = subprocess.Popen('echo "to stdout"', shell=True, stdout=subprocess.PIPE, )
        self.output = self.proc.communicate()[0]
        print(str(self.output))
