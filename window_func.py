import tkinter as tk
from tkinter import messagebox
import convert


class WindowFunc(tk.Toplevel):
    def __init__(self, master, database):
        super().__init__(master)

        self.database = database
        self.data_obj_dct = self.database.data_obj_dct

        self.master.withdraw()
        self.title("WindowFunc")
        self['background'] = '#9E9E9E'

        w = 640  # Width
        h = 475  # Height

        # Calculate Starting X and Y coordinates for Window
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Labels
        tk.Label(self, text='Результат', bg='#9E9E9E', font=('Arial', 12)).grid(row=0, column=0, sticky=tk.SW, padx=30, pady=10)
        tk.Label(self, text='Функції', bg='#9E9E9E', font=('Arial', 12)).grid(row=0, column=1, sticky=tk.SW, padx=30, pady=10)

        # Text
        self.result_text_widget = tk.Text(self, bg='#D9D9D9', bd=0, font=('Arial', 90), width=5, padx=10, pady=90, height=1, state=tk.DISABLED, wrap='word',)
        self.result_text_widget.grid(row=1, column=0, padx=30, rowspan=10)

        # Buttons
        funcs = [
            self.button_click_albums_in_year,
            self.button_click_songs_per_disk_avg,
            self.button_click_max_year,
            self.button_click_min_year,
            self.button_click_max_songs_count,
            self.button_click_min_songs_count,
            self.button_click_groups_count
            ]
        names = [
            'Альбомів у році',
            'Пісень у середньому',
            'Рік останнього альбому',
            'Рік першого альбому',
            'Максимум пісень',
            'Мінімум пісень',
            'Кількість груп',
        ]

        for i in range(7):
            tk.Button(self, height=2, width=25, text=names[i], bd=0, bg='#D9D9D9',
                      command=funcs[i]).grid(row=i+1, column=1, padx=5, pady=(0, 10))

        tk.Button(self, height=3, width=25, text='Назад', bd=0, bg='#D9D9D9',
                  command=self.button_click_back).grid(row=11, column=0, padx=30, pady=25, sticky=tk.SW)

        self.focus_force()

        # Key binds
        self.bind('<Escape>', self.button_click_back)
        # self.bind('<Return>', self.button_click_show)

    def button_click_back(self, event=None):
        self.withdraw()
        self.master.deiconify()
        return

    def update_result(self, text):
        self.result_text_widget.configure(state='normal')
        self.result_text_widget.delete('1.0', tk.END)
        self.result_text_widget.tag_configure("center", justify='center')
        self.result_text_widget.insert(tk.INSERT, text)
        self.result_text_widget.tag_add("center", '1.0', tk.END)
        self.result_text_widget.configure(state='disabled')

    def button_click_albums_in_year(self):
        search = WindowForm()
        search.wait_window()
        year = search.year
        if not year:
            return
        matched_objs = self.database.find(release_year=year)
        self.update_result(str(len(matched_objs)))

    def button_click_songs_per_disk_avg(self):
        songs_count = sum([obj.songs_count for obj in self.data_obj_dct.values()])
        albums_count = len(self.data_obj_dct)
        songs_per_disk_avg = str(songs_count / albums_count)
        self.update_result(songs_per_disk_avg)

    def button_click_max_year(self):
        max_year = max([obj.release_year for obj in self.data_obj_dct.values()])
        self.update_result(max_year)

    def button_click_min_year(self):
        min_year = min([obj.release_year for obj in self.data_obj_dct.values()])
        self.update_result(min_year)

    def button_click_max_songs_count(self):
        max_songs_count = max([obj.songs_count for obj in self.data_obj_dct.values()])
        self.update_result(max_songs_count)

    def button_click_min_songs_count(self):
        min_songs_count = min([obj.songs_count for obj in self.data_obj_dct.values()])
        self.update_result(min_songs_count)

    def button_click_groups_count(self):
        groups_count = len(set([obj.group_name for obj in self.data_obj_dct.values()]))
        self.update_result(groups_count)

class WindowForm(tk.Toplevel):
    def __init__(self):
        self.year = None
        super().__init__()
        self.title("WindowForm")
        self['background'] = '#9E9E9E'

        w = 186  # Width
        h = 130  # Height

        # Calculate Starting X and Y coordinates for Window
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        tk.Label(self, text='Уведіть рік:', bg='#9E9E9E', font=('Arial', 12)).grid(row=0, column=0, padx=20, pady=(10,0))

        self.year_entry = tk.Entry(self, bg='#D9D9D9', bd=0, font=('Arial', 12), width=9, justify='center')
        self.year_entry.grid(row=1, column=0, padx=20, pady=(10,0))
        self.year_entry.focus()

        tk.Button(self, height=2, width=20, text='Надіслати', bd=0, bg='#D9D9D9',
                  command=self.button_click_submit).grid(row=2, column=0, padx=20, pady=(10,0))

        self.bind('<Return>', self.button_click_submit)
        self.bind('<Escape>', self.button_click_back)

    def button_click_back(self, event=None):
        self.destroy()

    def button_click_submit(self, event=None):

        try:
            self.year = convert.str_to_int(self.year_entry.get())
        except TypeError:
            return

        if not self.year:
            messagebox.showerror('Помилка', 'Потрібно ввести рік')
            return

        self.destroy()