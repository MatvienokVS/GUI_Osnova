import tkinter as tk
from tkinter import *


def menu_main():

    main_menu = Menu()

    file_menu = Menu(main_menu, tearoff=0)
    # file_menu.add_command(label="Файл")
    # file_menu.add_command(label="Справочники")
    # file_menu.add_command(label="Отчёты")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=win_main.destroy)

    main_menu.add_cascade(label="Файл", menu=file_menu)
    main_menu.add_cascade(label="Справочники")
    main_menu.add_cascade(label="Отчёты")

    win_main.config(menu=main_menu)
    #menu_main = Menu(win_main)
    # win_main.config(menu=menu_main)

    #one_menu = Menu(file_main, tearoff=0)
    #file_menu.add_cascade(Label='Файл', menu=menu_main)

    #menu_main.add_cascade(Label='Файл', menu=file_menu)
