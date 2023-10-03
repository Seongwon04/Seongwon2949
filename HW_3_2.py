from tkinter import*
window = Tk()
fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]
num = 0
def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    Text1 = fnameList[num]
    label1.configure(text=Text1)
    

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    Text1 = fnameList[num]
    label1.configure(text=Text1)

window.geometry('700x100')
Text1 = fnameList[0]
label1 = Label(window, text = Text1, fg='blue', font=30)
button1 = Button(window, text='<< 이전', command=clickPrev)
button2 = Button(window, text='다음 >>', command=clickNext)

button1.pack(), label1.pack(), button2.pack()

button1.place(x=130, y=10)
button2.place(x=530, y=10)
label1.place(x=330, y=10)

window.mainloop()