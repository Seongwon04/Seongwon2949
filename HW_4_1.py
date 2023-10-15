from tkinter import*
from tkinter import messagebox
import sqlite3
window = Tk()
window.geometry('800x400')
window.resizable(0,0)
window.title('GUI 데이터 입력')

#데이터베이스 연결/ 데이터 입력
def Insert():
    con = sqlite3.connect('md202310604')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS userTable(사용자ID char(4), 사용자이름 char(15), 이메일 char(15), 출생연도 int)")
    data1 = E_UserID.get()
    data2 = E_UserName.get()
    data3 = E_Email.get()
    data4 = E_BirthYear.get()
    sql = "INSERT INTO userTable VALUES('"+data1+"', '"+data2+"', '"+data3+"', "+data4+")"
    try:
        cur.execute(sql)
    except:
        messagebox.showerror("오류", "데이터 입력 오류가 발생함")
    else:
        messagebox.showinfo("성공", "데이터 입력 성공")
    
    E_UserID.delete(0, END)
    E_UserName.delete(0, END)
    E_Email.delete(0, END)
    E_BirthYear.delete(0, END)

    con.commit()
    con.close()
    

#데이터베이스 데이터 불러오기/ 데이터 조회
def Display():
    con = sqlite3.connect('md202310604')
    cur = con.cursor()

    try:
        cur.execute('SELECT * FROM userTable')
    except:
        None
        
    data = cur.fetchall()
    if len(data) == 0:
        messagebox.showerror("오류", "조회할 데이터가 없습니다.")
    
    UserID.delete(0, END)
    UserName.delete(0, END)
    Email.delete(0, END)
    BirthYear.delete(0, END)

    UserID.insert(END, "사용자ID\n","----------")
    UserName.insert(END, "사용자이름\n", "----------")
    Email.insert(END, "이메일\n", "----------")
    BirthYear.insert(END, "출생연도\n", "----------")

    for item in data:
        UserID.insert(END, item[0])
        UserName.insert(END, item[1])
        Email.insert(END, item[2])
        BirthYear.insert(END, item[3])
    con.close()
    
    
#리스트박스, 엔트리 4개 생성
UserID = Listbox(window)
E_UserID = Entry(window)
UserName = Listbox(window)
E_UserName = Entry(window)
Email = Listbox(window)
E_Email = Entry(window)
BirthYear = Listbox(window)
E_BirthYear = Entry(window)

#입력 버튼 생성
button1 = Button(window) 
button1.config(text = '입력')
button1.config(width = 5)
button1.config(command = Insert)

#조회 버튼 생성
button2 = Button(window) 
button2.config(text = '조회')
button2.config(width = 5)
button2.config(command = Display)

#버튼, 리스트박스, 엔트리 크기 조정
E_UserID.config(width = 12)
E_UserName.config(width = 12)
E_Email.config(width = 12)
E_BirthYear.config(width = 12)
UserID.config(width = 25)
UserID.config(height = 19)
UserName.config(width = 25)
UserName.config(height = 19)
Email.config(width = 25)
Email.config(height = 19)
BirthYear.config(width = 25)
BirthYear.config(height = 19)

#리스트박스 색상 변경
UserID.config(bg='yellow')
UserName.config(bg='yellow')
Email.config(bg='yellow')
BirthYear.config(bg='yellow')

UserID.pack()
E_UserID.pack()
UserName.pack()
E_UserName.pack()
Email.pack()
E_Email.pack()
BirthYear.pack()
E_BirthYear.pack()
button1.pack()
button2.pack()

#버튼, 리스트박스, 엔트리 위치 조정
E_UserID.place(x=100,y=40)
E_UserName.place(x=220, y=40)
E_Email.place(x=340,y=40)
E_BirthYear.place(x=460,y=40)
button1.place(x=580,y=35)
button2.place(x=640,y=35)
UserID.place(x=15,y=80)
UserName.place(x=214,y=80)
Email.place(x=410,y=80)
BirthYear.place(x=605,y=80)

window.mainloop()