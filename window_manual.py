import tkinter as tk

class WindowManual(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master.withdraw()
        self.title("WindowManual")
        self['background'] = '#9E9E9E'

        w = 450  # Width
        h = 400  # Height

        # Calculate Starting X and Y coordinates for Window
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Labels
        tk.Label(self, text='Посібник користувача', bg='#9E9E9E', font=('Arial', 20)).grid(row=0, column=0, padx=40, pady=10)
        tk.Label(self, text='Ця програма — це система управління \nбазою даних музичних альбомів',
                 bg='#9E9E9E', font=('Arial', 15)).grid(row=1, column=0, padx=40, pady=0)

        # Buttons
        tk.Button(self, font=('Arial', 12), height=1, width=30, text='Як додати об’єкт до бази даних', justify='center', bd=0, bg='#D9D9D9', pady=3,
                  command=self.button_click_how_to_add).grid(row=2, column=0, pady=5)
        tk.Button(self, font=('Arial', 12), height=1, width=30, text='Як переглянути вміст бази даних', justify='center', bd=0, bg='#D9D9D9', pady=3,
                  command=self.button_click_how_to_show).grid(row=3, column=0, pady=5)
        tk.Button(self, font=('Arial', 12), height=1, width=30, text='Як редагувати об’єкт', justify='center', bd=0, bg='#D9D9D9', pady=3,
                  command=self.button_click_how_to_modify).grid(row=4, column=0, pady=5)
        tk.Button(self, font=('Arial', 12), height=1, width=30, text='Як видалити об’єкт', justify='center', bd=0, bg='#D9D9D9', pady=3,
                  command=self.button_click_how_to_remove).grid(row=5, column=0, pady=5)
        tk.Button(self, font=('Arial', 12), height=1, width=30, text='Як здійснювати пошук', justify='center', bd=0, bg='#D9D9D9', pady=3,
                  command=self.button_click_how_to_search).grid(row=6, column=0, pady=5)

        tk.Button(self, height=1, width=8, text='Назад', justify='center', bd=0, bg='#D9D9D9',
                  command=self.button_click_back).grid(row=7, column=0, pady=30, padx=10, sticky=tk.SW)

        self.focus_force()

        # Key binds
        self.bind('<Escape>', self.button_click_back)

    def button_click_back(self, event=None):
        self.withdraw()
        self.master.deiconify()
        return

    def button_click_how_to_add(self):
        WindowHowToAdd(self)

    def button_click_how_to_show(self):
        WindowHowToShow(self)

    def button_click_how_to_modify(self):
        WindowHowToModify(self)

    def button_click_how_to_remove(self):
        WindowHowToRemove(self)

    def button_click_how_to_search(self):
        WindowHowToSearch(self)

class WindowHowToAdd(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master.withdraw()
        self.title("WindowManual")
        self['background'] = '#9E9E9E'

        w = 450  # Width
        h = 400  # Height

        # Calculate Starting X and Y coordinates for Window
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        tk.Label(self,
                 text='Щоби додати об’єкт до бази, у головному вікні натисніть кнопку "Додати" — відкриється нове вікно. '
                      'Заповніть поля і натисніть кнопку "Додати" — з’явиться повідомлення про успіх чи некоректні дані.',
                 wraplength=400, justify='center', bg='#9E9E9E', font=('Arial', 14), pady=120, padx=30
                 ).grid(row=0, column=0)

        tk.Button(self, height=1, width=8, text='Назад', justify='center', bd=0, bg='#D9D9D9',
                  command=self.button_click_back).grid(row=1, column=0, pady=0, padx=10, sticky=tk.SW)

        self.bind('<Escape>', self.button_click_back)

        self.focus_force()

    def button_click_back(self, event=None):
        self.withdraw()
        self.master.deiconify()
        return

class WindowHowToShow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master.withdraw()
        self.title("WindowManual")
        self['background'] = '#9E9E9E'

        w = 450  # Width
        h = 400  # Height

        # Calculate Starting X and Y coordinates for Window
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        tk.Label(self,
                 text='Щоби переглянути вміст бази з можливість сортування, натисніть кнопку "Переглянути" — '
                      'відкриється нове вікно. Справа можна вибрати за якими критеріями відсортувати базу даних. '
                      'Аби відсортувати дані за спаданням, установіть прапорець "Reverse".'
                      'Натисніть кнопку "Показати", і результат з’явить у полі зліва.',
                         wraplength=400, justify='center', bg='#9E9E9E', font=('Arial', 14), pady=85, padx=30
                 ).grid(row=0, column=0)

        tk.Button(self, height=1, width=8, text='Назад', justify='center', bd=0, bg='#D9D9D9',
                  command=self.button_click_back).grid(row=1, column=0, pady=0, padx=10, sticky=tk.SW)

        self.bind('<Escape>', self.button_click_back)

        self.focus_force()

    def button_click_back(self, event=None):
        self.withdraw()
        self.master.deiconify()
        return

class WindowHowToModify(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master.withdraw()
        self.title("WindowManual")
        self['background'] = '#9E9E9E'

        w = 450  # Width
        h = 400  # Height

        # Calculate Starting X and Y coordinates for Window
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        tk.Label(self,
                 text='Щоби змінити об’єкт у базі, у головному вікні натисніть кнопку "Редагувати" — '
                      'відкриється нове вікно. Спершу потрібно ввести індекс об’єкта, який ви хочете змінити.'
                      'Потім натисніть кнопку "Знайти" — у полях з’являть дані об’єкта або з’явиться повідомлення, '
                      'що об’єкта з таким індексом немає. Після цього відредагуйте потрібні поля і натисніть "Редагувати".'
                      'Якщо всі дані коректні, з’явиться повідомлення про успіх, інакше — про помилку.',
                 wraplength=400, justify='center', bg='#9E9E9E', font=('Arial', 14), pady=50, padx=30
                 ).grid(row=0, column=0)

        tk.Button(self, height=1, width=8, text='Назад', justify='center', bd=0, bg='#D9D9D9',
                  command=self.button_click_back).grid(row=1, column=0, pady=0, padx=10, sticky=tk.SW)

        self.bind('<Escape>', self.button_click_back)

        self.focus_force()

    def button_click_back(self, event=None):
        self.withdraw()
        self.master.deiconify()
        return

class WindowHowToRemove(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master.withdraw()
        self.title("WindowManual")
        self['background'] = '#9E9E9E'

        w = 450  # Width
        h = 400  # Height

        # Calculate Starting X and Y coordinates for Window
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        tk.Label(self,
                 text='Щоби видалити об’єкт із бази, у головному вікні натисніть кнопку "Видалити" — відкриється нове вікно. '
                      'Уведіть індекс об’єкта, який хочете видалити, і натисніть кнопку "Видалити". '
                      'Якщо об’єкт із таким індексом у базі є, його буде видалено, і з’явиться повідомлення про це.',
                 wraplength=400, justify='center', bg='#9E9E9E', font=('Arial', 14), pady=95, padx=30
                 ).grid(row=0, column=0)

        tk.Button(self, height=1, width=8, text='Назад', justify='center', bd=0, bg='#D9D9D9',
                  command=self.button_click_back).grid(row=1, column=0, pady=0, padx=10, sticky=tk.SW)

        self.bind('<Escape>', self.button_click_back)

        self.focus_force()

    def button_click_back(self, event=None):
        self.withdraw()
        self.master.deiconify()
        return

class WindowHowToSearch(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master.withdraw()
        self.title("WindowManual")
        self['background'] = '#9E9E9E'

        w = 450  # Width
        h = 400  # Height

        # Calculate Starting X and Y coordinates for Window
        x = (self.winfo_screenwidth() / 2) - (w / 2)
        y = (self.winfo_screenheight() / 2) - (h / 2)

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        tk.Label(self,
                 text='Шукати об’єкти в базі можна в головному вікні. Заповніть потрібні поля і натисніть кнопку "Пошук".'
                      'У полі "Результат" з’явиляться об’єкти, які відповідають указаним даним.',
                 wraplength=400, justify='center', bg='#9E9E9E', font=('Arial', 14), pady=120, padx=30
                 ).grid(row=0, column=0)

        tk.Button(self, height=1, width=8, text='Назад', justify='center', bd=0, bg='#D9D9D9',
                  command=self.button_click_back).grid(row=1, column=0, pady=0, padx=10, sticky=tk.SW)

        self.bind('<Escape>', self.button_click_back)

        self.focus_force()

    def button_click_back(self, event=None):
        self.withdraw()
        self.master.deiconify()
        return
