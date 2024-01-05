import tkinter as tk
from album_class import Album
import convert
from tkinter import messagebox

class WindowAdd(tk.Toplevel):
    def __init__(self, master, database):
        self.database = database

        super().__init__(master)
        self.master.withdraw()
        self.title("WindowAdd")
        self['background'] = '#9E9E9E'

        w = 800  # Width
        h = 500  # Height

        # Calculate Starting X and Y coordinates for Window
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Labels
        tk.Label(self, text='Назва альбому', bg='#9E9E9E', font=('Arial', 12)).grid(row=0, column=0, sticky=tk.SW, padx=30, pady=10)
        tk.Label(self, text='Назва гурту', bg='#9E9E9E', font=('Arial', 12)).grid(row=0, column=1, sticky=tk.SW, pady=10)

        # Text
        self.album_name_text_widget = tk.Text(self, bg='#D9D9D9', bd=0, font=('Arial', 12), width=20, height=1, padx=10, pady=5)
        self.album_name_text_widget.grid(row=1, column=0, sticky=tk.W, padx=30)
        self.group_name_text_widget = tk.Text(self, bg='#D9D9D9', bd=0, font=('Arial', 12), width=20, height=1, padx=10, pady=5)
        self.group_name_text_widget.grid(row=1, column=1, sticky=tk.W, padx=0)

        # Labels
        tk.Label(self, text='Жанр', bg='#9E9E9E', font=('Arial', 12)).grid(row=2, column=0, sticky=tk.SW, padx=30, pady=10)
        tk.Label(self, text='Розповсюдник', bg='#9E9E9E', font=('Arial', 12)).grid(row=2, column=1, sticky=tk.SW, pady=10)

        # Text
        self.genre_text_widget = tk.Text(self, bg='#D9D9D9', bd=0, font=('Arial', 12), width=20, height=1, padx=10, pady=5)
        self.genre_text_widget.grid(row=3, column=0, sticky=tk.W, padx=30)
        self.distributor_text_widget = tk.Text(self, bg='#D9D9D9', bd=0, font=('Arial', 12), width=20, height=1, padx=10, pady=5)
        self.distributor_text_widget.grid(row=3, column=1, sticky=tk.W, padx=0)

        # Labels
        tk.Label(self, text='Кількість пісень', bg='#9E9E9E', font=('Arial', 12)).grid(row=4, column=0, sticky=tk.SW, padx=30, pady=10)
        tk.Label(self, text='Рік виходу', bg='#9E9E9E', font=('Arial', 12)).grid(row=4, column=1, sticky=tk.SW, pady=10)

        # Text
        self.songs_count_text_widget = tk.Text(self, bg='#D9D9D9', bd=0, font=('Arial', 12), width=20, height=1, padx=10, pady=5)
        self.songs_count_text_widget.grid(row=5, column=0, sticky=tk.W, padx=30)
        self.release_year_text_widget = tk.Text(self, bg='#D9D9D9', bd=0, font=('Arial', 12), width=20, height=1, padx=10, pady=5)
        self.release_year_text_widget.grid(row=5, column=1, sticky=tk.W, padx=0)

        # Labels
        tk.Label(self, text='Назви пісень', bg='#9E9E9E', font=('Arial', 12)).grid(row=0, column=2, sticky=tk.SW, padx=30, pady=10)

        # Text
        self.songs_names_text_widget = tk.Text(self, bg='#D9D9D9', bd=0, font=('Arial', 12), width=25, padx=10, pady=5, height=23)
        self.songs_names_text_widget.grid(row=1, column=2, padx=30, rowspan=10)

        # Buttons
        tk.Button(self, height=3, width=25, text='Назад', bd=0, bg='#D9D9D9',
                  command=self.button_click_back).grid(row=10, column=0, padx=30, pady=0)
        tk.Button(self, height=3, width=25, text='Додати', bd=0, bg='#D9D9D9',
                  command=self.button_click_add).grid(row=10, column=1, padx=0, pady=0)

        self.album_name_text_widget.focus_force()

        self.text_widgets = [
            self.album_name_text_widget,
            self.group_name_text_widget,
            self.genre_text_widget,
            self.distributor_text_widget,
            self.songs_count_text_widget,
            self.release_year_text_widget,
            self.songs_names_text_widget
            ]

        # Key binds
        self.bind('<Escape>', self.button_click_back)
        for text_widget in self.text_widgets:
            text_widget.bind('<Tab>', self.focus_next_field)
            text_widget.bind('<Shift-Tab>', self.focus_prev_field)

    def button_click_add(self):

        album_name = self.album_name_text_widget.get('1.0', 'end-1c')

        if not album_name:
            messagebox.showerror('Помилка', 'Уведіть назву альбому')
            return

        group_name = self.group_name_text_widget.get('1.0', 'end-1c')

        if not group_name:
            messagebox.showerror('Помилка', 'Уведіть назву гурту')
            return

        genre = self.genre_text_widget.get('1.0', 'end-1c')
        distributor = self.distributor_text_widget.get('1.0', 'end-1c')
        songs_names = convert.text_to_list(self.songs_names_text_widget.get('1.0', 'end-1c'))
        try:
            release_year = convert.str_to_int(self.release_year_text_widget.get('1.0', 'end-1c'))
            songs_count = convert.str_to_int(self.songs_count_text_widget.get('1.0', 'end-1c'))
        except TypeError:
            return

        new_album = Album(
            title=album_name,
            group_name=group_name,
            genre=genre,
            release_year=release_year,
            distributor=distributor,
            songs_count=songs_count,
            songs_names=songs_names
        )
        self.database.add(new_album)
        messagebox.showinfo('Успіх', 'Альбом додано')

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
