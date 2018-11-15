import tkinter as tk

window = tk.Tk();
window.title('tkinter entry')
window.geometry('500x500')
entry = tk.Entry(window, show=None)
entry.pack()


def insert_point():
    var = entry.get()
    text.insert('insert', var)


def insert_end():
    var = entry.get()
    # text.insert('end',var)
    text.insert(2.1, var)  # 1.0 行 列


button = tk.Button(window, text='insert point', width=15, height=2, command=insert_point)
button.pack()

button1 = tk.Button(window, text='insert end', width=15, height=2, command=insert_end)
button1.pack()

text = tk.Text(window, height=2)
text.pack()

window.mainloop()
