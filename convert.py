from tkinter import messagebox

def text_to_list(txt: str):
    return txt.split('\n')

def str_to_int(n: str):
    if not n:
        return 0

    if not n.replace('-', '', 1).isdecimal():
        messagebox.showerror('Помилка', f'Уведіть число')
        raise TypeError

    return int(n)
