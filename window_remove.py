import tkinter as tk
from tkinter import messagebox

class WindowRemove(tk.Toplevel):
    def __init__(self, master, database):
        self.database = database

        super().__init__(master)
        self.master.withdraw()
        self.title("WindowRemove")
        self['background'] = '#9E9E9E'

        w = 180  # Width
        h = 170  # Height

        # Calculate Starting X and Y coordinates for Window
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Label
        tk.Label(self, text='Індекс елемента', bg='#9E9E9E', font=('Arial', 12)).grid(row=0, column=0, padx=30, pady=10)

        # Text
        # self.index_text_widget = tk.Text(self, bg='#D9D9D9', bd=0, font=('Arial', 12), width=10, height=1, padx=10, pady=5)
        # self.index_text_widget.grid(row=1, column=0, padx=30)
        self.index_entry = tk.Entry(self, bg='#D9D9D9', bd=0, font=('Arial', 12), width=10, justify='center')
        self.index_entry.grid(row=1, column=0, padx=30)

        # Buttons
        tk.Button(self, height=1, width=15, text='Видалити', justify='center', bd=0, bg='#D9D9D9', pady=3,
                  command=self.button_click_remove).grid(row=2, column=0, pady=(10, 0))
        tk.Button(self, height=1, width=8, text='Назад', justify='center', bd=0, bg='#D9D9D9',
                  command=self.button_click_back).grid(row=3, column=0, pady=30, padx=10, sticky=tk.SW)

        self.index_entry.focus_force()

        # Key binds
        self.bind('<Escape>', self.button_click_back)
        self.bind('<Return>', self.button_click_remove)

    def button_click_back(self, event=None):
        self.withdraw()
        self.master.deiconify()

    def button_click_remove(self, event=None):
        index = self.index_entry.get()
        self.database.remove(index)
        self.index_entry.focus_force()


