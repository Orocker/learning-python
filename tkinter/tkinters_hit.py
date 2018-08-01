import tkinter as tk
window = tk.Tk();
window.title('My tk window')
window.geometry('500x500')
var = tk.StringVar()
label = tk.Label(window,textvariable=var,bg='green',font=('Arial',14),width=20,height=2)
label.pack()
# label.place()
show = False
def Click():
	global show
	if show == False:
		show = True
		var.set('You have Clicked me.')
	else:
		show = False
		var.set('')

button = tk.Button(window,text='Click me',width=15,height=2,command=Click)
button.pack()


window.mainloop()