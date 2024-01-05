import tkinter as tk
import json
from window_add import WindowAdd
from window_show import WindowShow
from window_manual import WindowManual
from window_modify import WindowModify
from window_func import WindowFunc
from window_remove import WindowRemove
import convert
from album_class import Album
from tkinter import messagebox

class AlbumsDatabase:

    # region Functionality
    def __init__(self, file):

        self.file = file

        with open(self.file, 'r') as f:
            self._data_dct = dict(json.load(f))

        self.increment = int(list(self._data_dct.keys())[-1])

        self.data_obj_dct = {}
        for key, element in self._data_dct.items():
            self.data_obj_dct[key] = Album(
                title=element['Title'],
                group_name=element['Group'],
                genre=element['Genre'],
                release_year=int(element['Year']),
                distributor=element['Distributor'],
                songs_count=int(element['SongsCount']),
                songs_names=element['SongsNames']
            )
    @staticmethod
    def data_to_str(data: dict) -> str:
        s = ''
        for i in data:
            s += f'Index: {i}\n'
            s += f'{str(data[i])}\n'
        return s

    def __str__(self):
        return self.data_to_str(self.data_obj_dct)

    def copy_data_obj_dct_to_data_dct(self):
        self._data_dct = {}

        for key, obj in self.data_obj_dct.items():
            self._data_dct[key] = {
                "Title": obj.title,
                "Group": obj.group_name,
                "Genre": obj.genre,
                "Year": obj.release_year,
                "Distributor": obj.distributor,
                "SongsCount": obj.songs_count,
                "SongsNames": obj.songs_names,
            }

    def write_to_file(self):

        self.copy_data_obj_dct_to_data_dct()

        with open(self.file, 'w') as f:
            json.dump(self._data_dct, f, indent=4)

    def is_index(self, index: str):
        if index not in self.data_obj_dct.keys():
            messagebox.showerror('Помилка', 'Об’єкта з таким індексом немає')
            return False
        return True

    def add(self, data_obj: object) -> None:
        self.increment += 1
        self.data_obj_dct[str(self.increment)] = data_obj

    def modify(self, index: str,
        title: str = None,
        group_name: str = None,
        genre: str = None,
        release_year: int = None,
        distributor: str = None,
        songs_count: int = None,
        songs_names: list = None) -> str:

        if not self.is_index(index):
            return

        self.data_obj_dct[index].title = title
        self.data_obj_dct[index].group_name = group_name
        self.data_obj_dct[index].genre = genre
        self.data_obj_dct[index].release_year = release_year
        self.data_obj_dct[index].distributor = distributor
        self.data_obj_dct[index].songs_count = songs_count
        self.data_obj_dct[index].songs_names = songs_names

        messagebox.showinfo('Успіх', f'Об’єкт {index} змінено')

    def remove(self, index: str):

        if not self.is_index(index):
            return

        del self.data_obj_dct[index]
        messagebox.showinfo('Успіх', 'Об’єкт видалено')

    def find(self, title: str = None,
        group_name: str = None,
        genre: str = None,
        release_year: int = None,
        release_year_from: int = None,
        release_year_to: int = None,
        distributor: str = None,
        songs_count: int = None,
        songs_names: list = None) -> str:

        result = {}

        for key, obj in self.data_obj_dct.items():

            if title and title.casefold() not in obj.title.casefold():
                continue

            if group_name and group_name.casefold() not in obj.group_name.casefold():
                continue

            if genre and genre.casefold() not in obj.genre.casefold():
                continue

            if distributor and distributor.casefold() not in obj.distributor.casefold():
                continue

            if release_year and convert.str_to_int(obj.release_year) != release_year:
                continue

            if release_year_from and convert.str_to_int(obj.release_year) < release_year_from:
                continue

            if release_year_to and convert.str_to_int(obj.release_year) > release_year_to:
                continue

            if songs_count and songs_count != convert.str_to_int(obj.songs_count):
                continue

            songs_matched = True

            if songs_names:
                for song_name in songs_names:
                    is_in_album = False
                    for song_name_database in obj.songs_names:
                        if song_name.casefold() in song_name_database.casefold():
                            is_in_album = True
                    if not is_in_album:
                        songs_matched = False
                        break
                if not songs_matched:
                    continue

            result[key] = obj

        return result

    def sort_database(self, key: object = lambda x: x[1].title, reverse: bool = False):
        sorted_database = dict(sorted(self.data_obj_dct.items(), key=key, reverse=reverse))
        return self.data_to_str(sorted_database)

    # endregion

class MainWindow(tk.Tk):
    def __init__(self, database):
        self.database = database

        super().__init__()
        self.title('MainWindow')
        self['background'] = '#9E9E9E'

        w = 850  # Width
        h = 925  # Height

        # Calculate Starting X and Y coordinates for Window
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Buttons
        tk.Button(self, height=3, width=20, text='Додати', bd=0, bg='#D9D9D9',
                  command=self.button_click_window_add).grid(row=0, column=0, padx=34, pady=(26,0))
        tk.Button(self, height=3, width=20, text='Переглянути', bd=0, bg='#D9D9D9',
                  command=self.button_click_window_show).grid(row=1, column=0, padx=34, pady=0)
        tk.Button(self, height=3, width=20, text='Видалити', bd=0, bg='#D9D9D9',
                  command=self.button_click_window_remove).grid(row=2, column=0, padx=34, pady=0)
        tk.Button(self, height=3, width=20, text='Редагувати', bd=0, bg='#D9D9D9',
                  command=self.button_click_window_modify).grid(row=3, column=0, padx=34, pady=0)
        tk.Button(self, height=3, width=20, text='Функції', bd=0, bg='#D9D9D9',
                  command=self.button_click_window_func).grid(row=4, column=0, padx=34, pady=0)
        tk.Button(self, height=3, width=20, text='Посібник', bd=0, bg='#D9D9D9',
                  command=self.button_click_window_manual).grid(row=11, column=0, padx=34, pady=0, sticky=tk.SW)

        # Label
        tk.Label(self, text='Результат пошуку', bg='#9E9E9E', font=('Arial', 12)).place(x=212, y=5)

        # Text
        self.result_text_widget = tk.Text(self, state=tk.DISABLED, bg='#D9D9D9', bd=0, width=74, wrap='word')
        self.result_text_widget.grid(row=0, column=1, rowspan=6, pady=35, columnspan=3, sticky=tk.W)

        # Labels
        tk.Label(self, text='Назва альбому', bg='#9E9E9E', font=('Arial', 12)).grid(row=7, column=1, sticky=tk.W)
        tk.Label(self, text='Назва групи', bg='#9E9E9E', font=('Arial', 12)).grid(row=7, column=2, sticky=tk.W)
        tk.Label(self, text='Жанр', bg='#9E9E9E', font=('Arial', 12)).grid(row=7, column=3, sticky=tk.W)

        # Entries
        self.album_name_entry = tk.Entry(self, bg='#D9D9D9', bd=0, font=('Arial', 12))
        self.album_name_entry.grid(row=8, column=1, sticky=tk.W, pady=10)
        self.group_name_entry = tk.Entry(self, bg='#D9D9D9', bd=0, font=('Arial', 12))
        self.group_name_entry.grid(row=8, column=2, sticky=tk.W, pady=10)
        self.genre_entry = tk.Entry(self, bg='#D9D9D9', bd=0, font=('Arial', 12))
        self.genre_entry.grid(row=8, column=3, sticky=tk.W, pady=10)

        # Frame
        frame = tk.Frame(self, bd=0, bg='#9E9E9E')
        frame.grid(row=9, column=1, sticky=tk.W, pady=10)

        # Labels
        tk.Label(frame, text='Рік виходу', bg='#9E9E9E', font=('Arial', 12)).grid(row=0, column=0, columnspan=2, sticky=tk.W)
        tk.Label(frame, text='Від', bg='#9E9E9E', font=('Arial', 10)).grid(row=1, column=0, sticky=tk.W)
        tk.Label(frame, text='До', bg='#9E9E9E', font=('Arial', 10)).grid(row=1, column=1, sticky=tk.W, padx=15)

        # Entries
        self.release_year_from_entry = tk.Entry(frame, bg='#D9D9D9', bd=0, font=('Arial', 12), width=9)
        self.release_year_from_entry.grid(row=2, column=0, sticky=tk.W, pady=0, padx=0)
        self.release_year_to_entry = tk.Entry(frame, bg='#D9D9D9', bd=0, font=('Arial', 12), width=9)
        self.release_year_to_entry.grid(row=2, column=1, sticky=tk.W, pady=0, padx=15)

        # Labels
        tk.Label(self, text='Розповсюдник', bg='#9E9E9E', font=('Arial', 12)).grid(row=9, column=2, sticky=tk.NW, pady=25)
        tk.Label(self, text='Кількість пісень', bg='#9E9E9E', font=('Arial', 12)).grid(row=9, column=3, sticky=tk.NW, pady=25)

        # Entries
        self.distributor_entry = tk.Entry(self, bg='#D9D9D9', bd=0, font=('Arial', 12))
        self.distributor_entry.place(x=427, y=574)
        self.songs_count_entry = tk.Entry(self, bg='#D9D9D9', bd=0, font=('Arial', 12))
        self.songs_count_entry.place(x=627, y=574)

        # Label
        tk.Label(self, text='Назви пісень', bg='#9E9E9E', font=('Arial', 12)).grid(row=10, column=1, sticky=tk.NW, pady=10)

        # Text
        self.songs_names_text_widget = tk.Text(self, bg='#D9D9D9', bd=0, width=51, height=15)
        self.songs_names_text_widget.grid(row=11, column=1, rowspan=1, pady=0, columnspan=2, sticky=tk.W)

        # Button Find
        tk.Button(self, height=3, width=20, text='Пошук', bd=0, bg='#D9D9D9',
                  command=self.button_click_find).grid(row=11, column=3, padx=34, pady=0, sticky=tk.NW)

        # Key binds
        self.bind('<Return>', self.button_click_find)
        self.bind('<Escape>', self.exit)
        self.bind('<F1>', self.button_click_window_manual)

    def button_click_find(self, event=None):

        group_name = self.group_name_entry.get()
        album_name = self.album_name_entry.get()
        genre = self.genre_entry.get()
        distributor = self.distributor_entry.get()
        songs_names = convert.text_to_list(self.songs_names_text_widget.get('1.0', 'end-1c'))

        try:
            release_year_from = convert.str_to_int(self.release_year_from_entry.get())
            release_year_to = convert.str_to_int(self.release_year_to_entry.get())
            songs_count = convert.str_to_int(self.songs_count_entry.get())
        except TypeError:
            return

        result = self.database.find (
            title=album_name,
            group_name=group_name,
            genre=genre,
            release_year_from=release_year_from,
            release_year_to=release_year_to,
            distributor=distributor,
            songs_count=songs_count,
            songs_names=songs_names
        )
        result = AlbumsDatabase.data_to_str(result)

        if not result:
            result = 'Пошук не дав результатів'

        self.result_text_widget.configure(state='normal')
        self.result_text_widget.delete('1.0', tk.END)
        self.result_text_widget.insert('1.0', result)
        self.result_text_widget.configure(state='disabled')

    def button_click_window_add(self):
        WindowAdd(self, self.database)

    def button_click_window_modify(self):
        WindowModify(self, self.database)

    def button_click_window_remove(self):
        WindowRemove(self, self.database)

    def button_click_window_show(self):
        WindowShow(self, self.database)

    def button_click_window_func(self):
        WindowFunc(self, self.database)

    def button_click_window_manual(self, event=None):
        WindowManual(self)

    def exit(self, event=None):
        if messagebox.askokcancel("Вихід", "Хочете вийти?"):
            database.write_to_file()
            self.destroy()

if __name__ == "__main__":
    database = AlbumsDatabase('database.json')
    app = MainWindow(database)
    def on_closing():
        if messagebox.askokcancel("Вихід", "Хочете вийти?"):
            database.write_to_file()
            app.destroy()

    app.protocol("WM_DELETE_WINDOW", on_closing)

    app.mainloop()
