import tkinter as tk
from tkinter import messagebox

def BT_Plass():
    a = float(entry1.get())
    b = float(entry2.get())
    c = a + b
    label.config(text=f"Ответ: {c}")

def BT_Manus():
    a = float(entry1.get())
    b = float(entry2.get())
    c = a - b
    label.config(text=f"Ответ: {c}")

def BT_Inmuj():
    a = float(entry1.get())
    b = float(entry2.get())
    c = a * b
    label.config(text=f"Ответ: {c}")

def BT_Dels():
    a = float(entry1.get())
    b = float(entry2.get())
    c = a / b
    label.config(text=f"Ответ: {c}")

window = tk.Tk()
window.title("Мое окно")
window.geometry("400x300")

entry1 = tk.Entry(window, width=10, font=60)
entry1.pack(pady=20)

entry2 = tk.Entry(window, width=10, font=60)
entry2.pack(pady=20)

frame = tk.Frame(window)
frame.pack(pady=20)

button1 = tk.Button(frame, text="+", width=10, height=2, command=BT_Plass, font=60)
button1.grid(row=0, column=0)

button2 = tk.Button(frame, text="-", width=10, height=2, command=BT_Manus, font=60)
button2.grid(row=0, column=1 )

button3 = tk.Button(frame, text="*", width=10, height=2, command=BT_Inmuj, font=60)
button3.grid(row=1, column=0 )

button4 = tk.Button(frame, text="/", width=10, height=2, command=BT_Dels, font=60)
button4.grid(row=1, column=1 )

label = tk.Label(text="Ответ: ")
label.pack()

window.mainloop()
