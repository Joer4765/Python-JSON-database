import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class WindowShow(tk.Toplevel):
    def __init__(self, master, database):

        self.database = database

        super().__init__(master)
        self.master.withdraw()
        self.title("WindowShow")
        self['background'] = '#9E9E9E'

        w = 800  # Width
        h = 500  # Height

        # Calculate Starting X and Y coordinates for Window
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Labels
        tk.Label(self, text='Результат', bg='#9E9E9E', font=('Arial', 12)).grid(row=0, column=0, sticky=tk.SW, padx=30, pady=10)

        # Text
        self.result_text_widget = tk.Text(self, bg='#D9D9D9', bd=0, font=('Arial', 12), width=55, padx=10, pady=5, height=19, state=tk.DISABLED, wrap='word')
        self.result_text_widget.grid(row=1, column=0, padx=30, rowspan=10)

        # Buttons
        tk.Button(self, height=3, width=25, text='Назад', bd=0, bg='#D9D9D9',
                  command=self.button_click_back).grid(row=11, column=0, padx=30, pady=25, sticky=tk.SW)

        tk.Button(self, height=3, width=25, text='Показати', bd=0, bg='#D9D9D9',
                  command=self.button_click_show).grid(row=11, column=1, padx=10, pady=25, sticky=tk.SW)

        # Label
        tk.Label(self, text='Сортування', bg='#9E9E9E', font=('Arial', 12)).grid(row=0, column=1, sticky=tk.SW, padx=30, pady=10)

        # Combos
        self.sort_params_combo_lst = []
        for i in range(6):
            combo_var = tk.StringVar()
            combo = ttk.Combobox(self, textvariable=combo_var)
            combo['values'] = ('', 'Назва альбому', 'Назва гурту', 'Жанр', 'Рік виходу', 'Розповсюдник', 'Кількість пісень')
            combo.state(["readonly"])
            combo.grid(row=i+1, column=1, sticky=tk.NW, padx=30, pady=0)
            self.sort_params_combo_lst.append(combo_var)

        # Checkbox
        self.reverse_var = tk.BooleanVar()
        tk.Checkbutton(self, text='Reverse', variable=self.reverse_var, onvalue=True, offvalue=False,
                       bg='#9E9E9E', bd=0, activebackground='#9E9E9E', activeforeground='#9E9E9E').grid(row=7, column=1)

        self.focus_force()

        # Key binds
        self.bind('<Escape>', self.button_click_back)
        self.bind('<Return>', self.button_click_show)

    def button_click_back(self, event=None):
        self.withdraw()
        self.master.deiconify()
        return

    def button_click_show(self, event=None):

        def combo_lst_to_content_lst(combo_lst: list) -> list:
            return [combo.get() for combo in combo_lst]

        def remove_blanks_lst(lst: list) -> list:
            while '' in lst:
                lst.remove('')
            return lst

        def is_all_different(lst: list) -> bool:
            if len(set(lst)) != len(lst):
                return False
            return True

        sort_params_lst = combo_lst_to_content_lst(self.sort_params_combo_lst)
        sort_params_lst_cleared = remove_blanks_lst(sort_params_lst)

        if not is_all_different(sort_params_lst_cleared):
            messagebox.showinfo('Некоректний ввід', 'Параметри сортування мають бути різні')
            return

        def sorter(x):

            dct = {'Назва альбому': x[1].title,
                   'Назва гурту': x[1].group_name,
                   'Жанр': x[1].genre,
                   'Рік виходу': x[1].release_year,
                   'Розповсюдник': x[1].distributor,
                   'Кількість пісень': x[1].songs_count}

            return [dct[i] for i in sort_params_lst_cleared]

        sorted_database_str = self.database.sort_database(key=sorter, reverse=self.reverse_var.get())

        self.result_text_widget.configure(state='normal')
        self.result_text_widget.delete('1.0', tk.END)
        self.result_text_widget.insert('1.0', sorted_database_str)
        self.result_text_widget.configure(state='disabled')