from tkinter import *
from tkinter import messagebox

root = Tk()
def notfound():
    messagebox.showinfo(title='Ой!', message='Раздел в разработке.')

def notfound2():
    messagebox.showerror(title='Ой!', message='Раздел в разработке.')



def chemistry():
    def calc_chem1():
        frame1 = Frame(win, bg='#f5f5f5')
        frame1.place(relwidth=1, relheight=1)
        label_heading1 = Label(frame1, text="Расчёт массы в-ва в растворе",
              font=("Verdana", 24),
              bg="#fafafa")
        label_heading1.pack()
        label_unhead = Label(frame1, text="Введите:",font=("Verdana"), bg="#fafafa")
        label_unhead.pack()
        massa = Entry(frame1)
        massa.pack()
        btn_success = Button(frame1,text = "Расчитать", command = '')
        btn_success.pack() 
    win = Toplevel(frame, relief=SUNKEN, bd=10, bg="#fafafa")
    win.title("Калькулятор по химии")
    win.geometry('800x500+350+100')
    label_heading = Label(win, text="Скоро тут что-то будет",
              font=("Verdana", 24),
              bg="#fafafa")
    label_heading.pack()
    btn1 = Button(win, text ="Вернуться назад", command = win.destroy)
    btn1.pack()
    btn2 = Button(win,text = "Расчёт массы в-ва в растворе", command = calc_chem1)
    btn2.pack()
    
    
root['bg']='#fafafa'
#root.iconbitmap('calculatori.ico')
root.title('Добро пожаловать!')
#root.wm_attributes('-alpha',0.995)
root.geometry('800x500+350+100')
root.resizable(width=False, height=False)

frame = Frame(root, bg='#fafafa')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

label = Label(frame,
              text="Межпредметный \n калькулятор",
              font=("Verdana", 24),
              bg="#fafafa")
label.pack()

label1 = Label(frame, text="Выберите:",font=("Verdana"), bg="#fafafa")
label1.pack()

btn_predmet1= Button(frame,
                     text="Геометрия", 
                     width=16,
                     height=2,
                     padx="10",
                     pady="5",                     
                     command=notfound) 
btn_predmet1.pack()

btn_predmet2= Button(frame,
                     text="Физика", 
                     width=16,
                     height=2,
                     padx="10",
                     pady="5",
                     command=notfound2) 
btn_predmet2.pack()

btn_predmet3= Button(frame,
                     text="Химия", 
                     width=16,
                     height=2,
                     padx="10",
                     pady="5",
                     command=chemistry)
btn_predmet3.pack()

root.mainloop()
