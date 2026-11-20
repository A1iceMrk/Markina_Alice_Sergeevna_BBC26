'''
Разработать интерфейс:
1) Главное окно
2) Текстовые элементы
3) Поле ввода
4) Кнопка
5) Выбор параметра (to do list)
6) Вывод результатов
7) Обработка событий
8) Проверка данных
9) Диалоговое окно
10) Компановка
'''

import tkinter as tk
from tkinter import messagebox

def add_task(event = None):
    text = entry.get().strip()
    if text == "":
        messagebox.showwarning('Внимание!', 'Введите название задачи!')
        return
    if important_var.get():
        task_line = f"[ВАЖНО] {text}"
    else:
        task_line = text
    listbox.insert(tk.END, task_line)
    entry.delete(0, tk.END)
    important_var.set(False)

def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning('Внимание!', 'Выберите задачу в списке для удаления!')
        return
    answer = messagebox.askyesno('Удаление.', 'Удалить выбранную задачу?')
    if answer:
        listbox.delete(selected[0])

root = tk.Tk()
root.title('To-Do List')
root.geometry('400x320')

label = tk.Label(root, text='Список задач', font=('Arial', 14))
label.pack(pady=10)

entry = tk.Entry(root, width=30, font=('Arial', 11))
entry.pack(pady=5)

important_var = tk.BooleanVar()
check = tk.Checkbutton(root, text='Важная задача', variable=important_var)
check.pack(pady=5)

add_button = tk.Button(root, text='Добавить задачу', command=add_task)
add_button.pack(pady=5)

listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)

delete_button = tk.Button(root, text='Удалить выбранную', command=delete_task)
delete_button.pack(pady=5)

entry.bind('<Return>', add_task)

root.mainloop()