import csv
from doctest import master
import tkinter as tk
from tkinter.tix import Tree
import tkinter.ttk as ttk
from tkinter import Menu


class Operation(tk.Tk):
    def __init__(self, path):
        super().__init__()
        self.title("Подразделения")
        h = 500
        w = 300
        self.geometry(f"{h}x{w}+300+150")
        self.minsize(h, w)
        self.maxsize(1000, 600)
        self.frame_1 = tk.Frame(master, bg='#abcdef').place(
            relx=0, rely=0, relwidth=1, relheight=0.15)
        self.frame_2 = tk.Frame(master, bg='#00abdd').place(
            relx=0, rely=0.08, relwidth=1, relheight=1)

        # Меню
        def menuFormMain():
            f_menu = Menu(self.master)
            self.config(menu=f_menu)

            file_menu = Menu(f_menu, tearoff=0)

            f_menu.add_cascade(label="Файл", menu=file_menu)
            file_menu.add_command(label="Выход", command=self.destroy)

        menuFormMain()


if __name__ == "__main__":
    oper = Operation(path=".")
    oper.mainloop()
