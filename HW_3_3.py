from tkinter import*
window = Tk()
window.geometry('140x250')
window.resizable(0,0)

def Insert():
    ToDo.insert(END, ent.get())

def Delete():
    ToDo.delete(ToDo.curselection())

ToDo = Listbox(window)
ToDo.config(selectmode='single')
ToDo.config(height = 9)

ent = Entry(window)

button1 = Button(window)
button1.config(text='Add Task')
button1.config(width=10)
button1.config(command=Insert)

button2 = Button(window)
button2.config(text='Delete Task')
button2.config(width=10)
button2.config(command=Delete)

label1 = Label(window)
label1.config(text='Add a Task')

label1.pack()
ent.pack()
button1.pack()
ToDo.pack()
button2.pack()
button2.place(x=30,y=220)

window.mainloop()