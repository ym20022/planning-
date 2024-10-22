import tkinter as tk
from tkinter import messagebox
import sqlite3

def create_task_table():
    conn = sqlite3.connect('task_manager.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 task_name TEXT, 
                 task_date TEXT, 
                 task_time TEXT, 
                 notes TEXT, 
                 location TEXT, 
                 emails TEXT)''')
    conn.commit()
    conn.close()


def add_task():
    task_name = task_name_entry.get()
    task_date = task_date_entry.get()
    task_time = task_time_entry.get()
    notes = notes_entry.get("1.0", "end-1c")
    location = location_entry.get()
    emails = emails_entry.get()

    conn = sqlite3.connect('task_manager.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task_name, task_date, task_time, notes, location, emails) VALUES (?, ?, ?, ?, ?, ?)",
              (task_name, task_date, task_time, notes, location, emails))
    conn.commit()
    conn.close()
    messagebox.showinfo("Task Added", "Task has been added successfully!")

root = tk.Tk()
root.title("Планировщик задач")


tk.Label(root, text="Название задачи:").pack()
task_name_entry = tk.Entry(root)
task_name_entry.pack()

tk.Label(root, text="Дата (гггг-мм-дд):").pack()
task_date_entry = tk.Entry(root)
task_date_entry.pack()

tk.Label(root, text="Время (чч:мм):").pack()
task_time_entry = tk.Entry(root)
task_time_entry.pack()

tk.Label(root, text="Заметки:").pack()
notes_entry = tk.Text(root, height=4)
notes_entry.pack()

tk.Label(root, text="Место события:").pack()
location_entry = tk.Entry(root)
location_entry.pack()

tk.Label(root, text="Email участников (через запятую):").pack()
emails_entry = tk.Entry(root)
emails_entry.pack()

add_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_button.pack()


create_task_table()

root.mainloop()
