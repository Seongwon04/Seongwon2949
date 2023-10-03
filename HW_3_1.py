from tkinter import*
window = Tk()
window.geometry('600x500')
label1 = Label(window, text = '좋아하는 동물 투표', font = ('궁서체',30), fg='green') #레이블1 텍스트
window.title('애완동물 선택하기') #제목

def  showImage() :                    #사진변환, 사진보기
    if chk.get() == 1 :
        label2.configure(image=dog_photo)        
    elif chk.get() == 2 :
        label2.configure(image=cat_photo)
    else :
        label2.configure(image=rabbit_photo)
    label2.pack()

def myFunc():   #패스
    pass

button1 = Button(window, text='사진 보기', command=showImage) #버튼생성
    
chk = IntVar()
rb1 = Radiobutton(window, text = "강아지", variable = chk, value = 1, command = myFunc)
rb2 = Radiobutton(window, text = "고양이", variable = chk, value = 2, command = myFunc)
rb3 = Radiobutton(window, text = "토끼", variable = chk, value = 3, command = myFunc)

dog_photo = PhotoImage(file='dog.gif')
cat_photo = PhotoImage(file='cat.gif')
rabbit_photo = PhotoImage(file='rabbit.gif')

label2 = Label(window, image=dog_photo)
label1.pack(), rb1.pack(), rb2.pack(), rb3.pack(), button1.pack()

window.mainloop()