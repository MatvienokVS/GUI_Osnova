import csv
from doctest import master
from posixpath import relpath
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Label, Menu
import calendar


class App(tk.Tk):
    def __init__(self, path):
        super().__init__()
        self.title("Руководитель")
        h = 1000
        w = 600
        self.geometry(f"{h}x{w}+300+150")
        self.minsize(h, w)
        self.maxsize(1200, 700)
        #self.iconphoto(False, tk.PhotoImage(file='photo.png'))
        # Фрейм левый верхний
        self.frame_1 = tk.Frame(master, bg='#abcdef').place(
            relx=0, rely=0, relwidth=0.2, relheight=1)
        # Фрейм правый верхний
        self.frame_2 = tk.Frame(master, bg='#ab6632').place(
            relx=0.2, rely=0, relwidth=0.8, relheight=0.5)
        # Фрейм нижний
        self.frame_3 = tk.Frame(master, bg='#00abdd').place(
            relx=0.2, rely=0.5, relwidth=1, relheight=0.5)

        # Меню
        def menu():
            f_menu = Menu(self.master)
            self.config(menu=f_menu)
            # Меню файл
            file_menu = Menu(f_menu, tearoff=0)
            f_menu.add_cascade(label="Файл", menu=file_menu)
            file_menu.add_command(label="Открыть")
            file_menu.add_command(label="Сохранить...")
            file_menu.add_command(label="Выход", command=self.destroy)
            # Меню справочники
            help_menu = Menu(f_menu, tearoff=0)
            f_menu.add_cascade(label="Справочники", menu=help_menu)
            help_menu_2 = Menu(help_menu, tearoff=0)
            help_menu.add_cascade(label="Справочники", menu=help_menu_2)
            help_menu_2.add_command(label="Сотрудники")
            help_menu_2.add_command(label="Организации")
            help_menu_2.add_command(label="Подразделения")

            # Меню помощь
            question_menu = Menu(f_menu, tearoff=0)
            f_menu.add_cascade(label="?", menu=question_menu)
            question_menu.add_command(label="Версия программы")

        menu()

        def cbx_otdel():
            self.cbx_otdel = ttk.Combobox(
                self.frame_2, values=('ИП"Пенкин" ИП"Матвиенок"')).place(relx=0.7, rely=0.01, relwidth=0.295)
        cbx_otdel()

        def lbl_frame_2():
            self.lbl_otdel = tk.Label(
                text='Наименование организации', bg='#ab6632', font=('Franklin Gothic Book', 10, 'bold')).place(relx=0.5, rely=0.01)
            self.lbl_date = tk.Label(
                text='Дата', bg='#ab6632', font=('Franklin Gothic Book', 10)).place(relx=0.657, rely=0.05)

        lbl_frame_2()


if __name__ == "__main__":
    apps = App(path=".")
    apps.mainloop()
