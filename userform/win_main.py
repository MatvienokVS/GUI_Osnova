# Создание главной формы проекта GUI_Osnova

import tkinter as tk
from tkinter import *


win_main = tk.Tk()

heidth = 1500
width = 800


win_main.geometry(f'{heidth}x{width}+200+100')			# Геометрия окна
win_main.config(bg='#00abdd')							# Фон окна
win_main.title('Бюджет движения денежных средств')		# Название окна
win_main.resizable(False, False)						# Запрет на изменение размера
icon = PhotoImage(file='userform/photo.png')			# Добавление иконки
win_main.iconphoto(False, icon)

# main_menu()


win_main.mainloop()
