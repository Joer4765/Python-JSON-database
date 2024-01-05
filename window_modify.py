import tkinter as tk
from tkinter import messagebox
import convert

class WindowModify(tk.Toplevel):
    def __init__(self, master, database):
        self.database = database
        self.index = None

        super().__init__(master)
        self.master.withdraw()
        self.title("WindowModify")
        self['background'] = '#9E9E9E'

        w = 800  # Width
        h = 500  # Height

        # Calculate Starting X and Y coordinates for Window
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Labels
        tk.Label(self, text='Назва альбому', bg='#9E9E9E', font=('Arial', 12)).grid(row=0, column=0, sticky=tk.SW, padx=30, pady=0)
        tk.Label(self, text='Назва групи', bg='#9E9E9E', font=('Arial', 12)).grid(row=0, column=1, sticky=tk.SW, pady=0)

        # Text
        self.album_name_text_widget = tk.Text(self, bg='#D9D9D9', bd=0, font=('Arial', 12), width=20, height=1, padx=10, pady=5)
        self.album_name_text_widget.grid(row=1, column=0, sticky=tk.W, padx=30)
        self.group_name_text_widget = tk.Text(self, bg='#D9D9D9', bd=0, font=('Arial', 12), width=20, height=1, padx=10, pady=5)
        self.group_name_text_widget.grid(row=1, column=1, sticky=tk.W, padx=0)

        # Labels
        tk.Label(self, text='Жанр', bg='#9E9E9E', font=('Arial', 12)).grid(row=2, column=0, sticky=tk.SW, padx=30, pady=0)
        tk.Label(self, text='Розповсюдник', bg='#9E9E9E', font=('Arial', 12)).grid(row=2, column=1, sticky=tk.SW, pady=0)

        # Text
        self.genre_text_widget = tk.Text(self, bg='#D9D9D9', bd=0, font=('Arial', 12), width=20, height=1, padx=10, pady=5)
        self.genre_text_widget.grid(row=3, column=0, sticky=tk.W, padx=30)
        self.distributor_text_widget = tk.Text(self, bg='#D9D9D9', bd=0, font=('Arial', 12), width=20, height=1, padx=10, pady=5)
        self.distributor_text_widget.grid(row=3, column=1, sticky=tk.W, padx=0)

        # Labels
        tk.Label(self, text='Кількість пісень', bg='#9E9E9E', font=('Arial', 12)).grid(row=4, column=0, sticky=tk.SW, padx=30, pady=0)
        tk.Label(self, text='Рік виходу', bg='#9E9E9E', font=('Arial', 12)).grid(row=4, column=1, sticky=tk.SW, pady=0)

        # Text
        self.songs_count_text_widget = tk.Text(self, bg='#D9D9D9', bd=0, font=('Arial', 12), width=20, height=1, padx=10, pady=5)
        self.songs_count_text_widget.grid(row=5, column=0, sticky=tk.W, padx=30)
        self.release_year_text_widget = tk.Text(self, bg='#D9D9D9', bd=0, font=('Arial', 12), width=20, height=1, padx=10, pady=5)
        self.release_year_text_widget.grid(row=5, column=1, sticky=tk.W, padx=0)

        # Label
        tk.Label(self, text='Назви пісень', bg='#9E9E9E', font=('Arial', 12)).grid(row=0, column=2, sticky=tk.SW, padx=30, pady=10)

        # Text
        self.songs_names_text_widget = tk.Text(self, bg='#D9D9D9', bd=0, font=('Arial', 12), width=25, padx=10, pady=5, height=23)
        self.songs_names_text_widget.grid(row=1, column=2, padx=30, rowspan=10)

        # Frame
        frame = tk.Frame(self, bg='#9E9E9E')
        frame.grid(row=6, column=0, rowspan=4, columnspan=2)

        # Label
        tk.Label(frame, text='Індекс елемента', bg='#9E9E9E', font=('Arial', 12)).grid(row=0, column=0)

        # Text
        self.index_text_widget = tk.Text(frame, bg='#D9D9D9', bd=0, font=('Arial', 12), width=4, height=1, padx=10, pady=2)
        self.index_text_widget.grid(row=1, column=0, pady=5)

        # Buttons
        tk.Button(frame, height=1, width=8, text='Знайти', justify='center', bd=0, bg='#D9D9D9',
                  command=self.button_click_find).grid(row=2, column=0, pady=5)

        # Buttons
        tk.Button(self, height=3, width=25, text='Назад', bd=0, bg='#D9D9D9',
                  command=self.button_click_back).grid(row=10, column=0, padx=30, pady=0)
        tk.Button(self, height=3, width=25, text='Редагувати', bd=0, bg='#D9D9D9',
                  command=self.button_click_modify).grid(row=10, column=1, padx=0, pady=0)

        self.index_text_widget.focus_force()

        self.text_widgets = [
            self.album_name_text_widget,
            self.group_name_text_widget,
            self.genre_text_widget,
            self.distributor_text_widget,
            self.songs_count_text_widget,
            self.release_year_text_widget,
            self.songs_names_text_widget,
        ]

        # Key binds
        self.bind('<Escape>', self.button_click_back)
        for text_widget in self.text_widgets:
            text_widget.bind('<Tab>', self.focus_next_field)
            text_widget.bind('<Shift-Tab>', self.focus_prev_field)
            text_widget.bind('<Return>', self.button_click_modify)

        self.index_text_widget.bind('<Tab>', self.focus_next_field)
        self.index_text_widget.bind('<Shift-Tab>', self.focus_prev_field)
        self.index_text_widget.bind('<Return>', self.button_click_find)

    def button_click_find(self, event=None):
        self.index = self.index_text_widget.get('1.0', 'end-1c')

        self.album_name_text_widget.delete('1.0', tk.END)
        self.group_name_text_widget.delete('1.0', tk.END)
        self.genre_text_widget.delete('1.0', tk.END)
        self.distributor_text_widget.delete('1.0', tk.END)
        self.songs_count_text_widget.delete('1.0', tk.END)
        self.release_year_text_widget.delete('1.0', tk.END)
        self.songs_names_text_widget.delete('1.0', tk.END)

        if not self.database.is_index(self.index):
            return

        data_obj_dct = self.database.data_obj_dct

        self.album_name_text_widget.insert('1.0', data_obj_dct[self.index].title)
        self.group_name_text_widget.insert('1.0', data_obj_dct[self.index].group_name)
        self.genre_text_widget.insert('1.0', data_obj_dct[self.index].genre)
        self.distributor_text_widget.insert('1.0', data_obj_dct[self.index].distributor)
        self.songs_count_text_widget.insert('1.0', data_obj_dct[self.index].songs_count)
        self.release_year_text_widget.insert('1.0', data_obj_dct[self.index].release_year)
        self.songs_names_text_widget.insert('1.0', '\n'.join(data_obj_dct[self.index].songs_names))
        return "break"

    def button_click_modify(self):

        if not self.index:
            messagebox.showerror('Помилка', 'Спершу знайдіть об’єкт')
            return

        album_name = self.album_name_text_widget.get('1.0', 'end-1c')
        group_name = self.group_name_text_widget.get('1.0', 'end-1c')
        genre = self.genre_text_widget.get('1.0', 'end-1c')
        distributor = self.distributor_text_widget.get('1.0', 'end-1c')
        songs_names = convert.text_to_list(self.songs_names_text_widget.get('1.0', 'end-1c'))
        try:
            release_year = convert.str_to_int(self.release_year_text_widget.get('1.0', 'end-1c'))
            songs_count = convert.str_to_int(self.songs_count_text_widget.get('1.0', 'end-1c'))
        except TypeError:
            return

        self.database.modify(
            index=self.index,
            title=album_name,
            group_name=group_name,
            genre=genre,
            release_year=release_year,
            distributor=distributor,
            songs_count=songs_count,
            songs_names=songs_names
        )
        return "break"

    @staticmethod
    def focus_prev_field(event):
        event.widget.tk_focusPrev().focus()
        return "break"

    @staticmethod
    def focus_next_field(event):
        event.widget.tk_focusNext().focus()
        return "break"


    def button_click_back(self, event=None):
        self.withdraw()
        self.master.deiconify()
        return




