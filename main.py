import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import datetime

win = Tk()
win.geometry('420x450')
win.title('Межпредметный калькулятор')
win.resizable(height = False, width = False)

masf = []
now = datetime.datetime.now()   
s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Запуск программы'
masf.append(s)

def GEOM():
    rad_g1.grid_remove()
    rad_g2.grid_remove()
    rad_g3.grid_remove()
    rad_g4.grid_remove()
    rad_g5.grid_remove()
    rad_f1.grid_remove()
    rad_f2.grid_remove()
    rad_f3.grid_remove()
    rad_f4.grid_remove()
    rad_f5.grid_remove()
    rad_f6.grid_remove()
    rad_x1.grid_remove()
    rad_gd1.grid_remove()
    rad_gd2.grid_remove()
    rad_gd3.grid_remove()
    rad_gd4.grid_remove()
    rad_gd5.grid_remove()
    rad_gd6.grid_remove()
    rad_gd1a.grid_remove()
    rad_gd2a.grid_remove()
    rad_gd3a.grid_remove()
    rad_gd4a.grid_remove()
    rad_gd5a.grid_remove()
    rad_gd7.grid_remove()
    rad_gd7a.grid_remove()
    rad_gd8.grid_remove()
    rad_gd8a.grid_remove()
    rad_gd10.grid_remove()
    rad_gd10a.grid_remove()
    rad_gd11.grid_remove()
    rad_gd12.grid_remove()
    rad_gd13.grid_remove()
    rad_gd13a.grid_remove()
    rad_gd14.grid_remove()
    rad_gd15.grid_remove()
    rad_gd16.grid_remove()
    rad_g1.grid(column=0, row=5, sticky=W)
    rad_g2.grid(column=0, row=6, sticky=W)
    rad_g3.grid(column=0, row=7, sticky=W)
    rad_g4.grid(column=0, row=8, sticky=W)
    rad_g5.grid(column=0, row=9, sticky=W) #выбор калькулятора

def FIZ():
    rad_g1.grid_remove()
    rad_g2.grid_remove()
    rad_g3.grid_remove()
    rad_g4.grid_remove()
    rad_g5.grid_remove()
    rad_f1.grid_remove()
    rad_f2.grid_remove()
    rad_f3.grid_remove()
    rad_f4.grid_remove()
    rad_f5.grid_remove()
    rad_f6.grid_remove()
    rad_x1.grid_remove()
    rad_gd1.grid_remove()
    rad_gd2.grid_remove()
    rad_gd3.grid_remove()
    rad_gd4.grid_remove()
    rad_gd5.grid_remove()
    rad_gd6.grid_remove()
    rad_gd7.grid_remove()
    rad_gd8.grid_remove()
    rad_gd10.grid_remove()
    rad_gd11.grid_remove()
    rad_gd12.grid_remove()
    rad_gd13.grid_remove()
    rad_gd14.grid_remove()
    rad_gd15.grid_remove()
    rad_gd16.grid_remove()
    rad_gd1.grid_remove()
    rad_gd2.grid_remove()
    rad_gd3.grid_remove()
    rad_gd4.grid_remove()
    rad_gd5.grid_remove()
    rad_gd6.grid_remove()
    rad_gd1a.grid_remove()
    rad_gd2a.grid_remove()
    rad_gd3a.grid_remove()
    rad_gd4a.grid_remove()
    rad_gd5a.grid_remove()
    rad_gd7.grid_remove()
    rad_gd7a.grid_remove()
    rad_gd8.grid_remove()
    rad_gd8a.grid_remove()
    rad_gd10.grid_remove()
    rad_gd10a.grid_remove()
    rad_gd11.grid_remove()
    rad_gd12.grid_remove()
    rad_gd13.grid_remove()
    rad_gd13a.grid_remove()
    rad_gd14.grid_remove()
    rad_gd15.grid_remove()
    rad_gd16.grid_remove()
    rad_f1.grid(column=0, row=5, sticky=W)
    rad_f2.grid(column=0, row=6, sticky=W)
    rad_f3.grid(column=0, row=7, sticky=W)
    rad_f4.grid(column=0, row=8, sticky=W)
    rad_f5.grid(column=0, row=9, sticky=W)
    rad_f6.grid(column=0, row=10, sticky=W) #выбор калькулятора
    lab3 = Label(win, text='Доп. выбор:', fg='SystemButtonFace')
    lab3.grid(column=0, row=11, sticky=W)
    radio_var1.set(-1)


def XIM():
    rad_g1.grid_remove()
    rad_g2.grid_remove()
    rad_g3.grid_remove()
    rad_g4.grid_remove()
    rad_g5.grid_remove()
    rad_f1.grid_remove()
    rad_f2.grid_remove()
    rad_f3.grid_remove()
    rad_f4.grid_remove()
    rad_f5.grid_remove()
    rad_f6.grid_remove()
    rad_x1.grid_remove()
    rad_gd1.grid_remove()
    rad_gd2.grid_remove()
    rad_gd3.grid_remove()
    rad_gd4.grid_remove()
    rad_gd5.grid_remove()
    rad_gd6.grid_remove()
    rad_gd7.grid_remove()
    rad_gd8.grid_remove()
    rad_gd10.grid_remove()
    rad_gd11.grid_remove()
    rad_gd12.grid_remove()
    rad_gd13.grid_remove()
    rad_gd14.grid_remove()
    rad_gd15.grid_remove()
    rad_gd16.grid_remove()
    rad_gd1.grid_remove()
    rad_gd2.grid_remove()
    rad_gd3.grid_remove()
    rad_gd4.grid_remove()
    rad_gd5.grid_remove()
    rad_gd6.grid_remove()
    rad_gd1a.grid_remove()
    rad_gd2a.grid_remove()
    rad_gd3a.grid_remove()
    rad_gd4a.grid_remove()
    rad_gd5a.grid_remove()
    rad_gd7.grid_remove()
    rad_gd7a.grid_remove()
    rad_gd8.grid_remove()
    rad_gd8a.grid_remove()
    rad_gd10.grid_remove()
    rad_gd10a.grid_remove()
    rad_gd11.grid_remove()
    rad_gd12.grid_remove()
    rad_gd13.grid_remove()
    rad_gd13a.grid_remove()
    rad_gd14.grid_remove()
    rad_gd15.grid_remove()
    rad_gd16.grid_remove()
    rad_x1.grid(column=0, row=5, sticky=W) #выбор калькулятора
    lab3 = Label(win, text='Доп. выбор:', fg='SystemButtonFace')
    lab3.grid(column=0, row=11, sticky=W)
    radio_var1.set(-1)

exporting = open("output.txt", "w")
exporting.write('----===[Расчеты]===----' + '\n\n')
count = 0
k_fiz = 0
k_xim = 0
k_math = 0

def G1():
    rad_gd1.grid_remove()
    rad_gd2.grid_remove()
    rad_gd3.grid_remove()
    rad_gd4.grid_remove()
    rad_gd5.grid_remove()
    rad_gd6.grid_remove()
    rad_gd1a.grid_remove()
    rad_gd2a.grid_remove()
    rad_gd3a.grid_remove()
    rad_gd4a.grid_remove()
    rad_gd5a.grid_remove()
    rad_gd7.grid_remove()
    rad_gd7a.grid_remove()
    rad_gd8.grid_remove()
    rad_gd8a.grid_remove()
    rad_gd10.grid_remove()
    rad_gd10a.grid_remove()
    rad_gd11.grid_remove()
    rad_gd12.grid_remove()
    rad_gd13.grid_remove()
    rad_gd13a.grid_remove()
    rad_gd14.grid_remove()
    rad_gd15.grid_remove()
    rad_gd16.grid_remove()
    rad_gd1.grid(column=0, row=12, sticky=W)
    rad_gd2.grid(column=0, row=13, sticky=W)
    rad_gd3.grid(column=0, row=14, sticky=W)
    rad_gd4.grid(column=0, row=15, sticky=W)
    rad_gd5.grid(column=0, row=16, sticky=W)
    rad_gd6.grid(column=0, row=17, sticky=W)
    lab3 = Label(win, text='Доп. выбор:', fg='black')
    lab3.grid(column=0, row=11, sticky=W)


def G1cub():
    win_g = Toplevel()
    win_g.title('Расчёт объёма куба')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт объёма куба'
    masf.append(s) 

    def G1cub1():
        if (ent_gcub1.get() == ''):
            lab_gcub3.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_gcub1.get().isdigit()) == False:
            lab_gcub3.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gcub3.configure(text=str(int(ent_gcub1.get()) ** 3), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт объёма куба ' + '\n' + 'Сторона a = ' + ent_gcub1.get() + '\t' + '--> ' + str(int(ent_gcub1.get()) ** 3) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_gcub3.configure(text='')
        ent_gcub1.delete(0, END)

    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_gcub1 = Label(win_g, text='Введите сторону куба:', padx = 3, pady = 2)
    lab_gcub2 = Label(win_g, text='Ответ:', padx = 3, pady = 2)
    lab_gcub3 = Label(win_g, text='')
    lab_gcub1.grid(column=0, row=0, sticky=W)
    lab_gcub2.grid(column=0, row=1, sticky=W)
    lab_gcub3.grid(column=1, row=1, sticky=W)

    ent_gcub1 = Entry(win_g, width=10)
    ent_gcub1.grid(column=1, row=0, sticky=W)
    ent_gcub1.focus_set()

    global photo
    photo = tk.PhotoImage(file = './img/volume_cube.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.30, rely=0.30)

    but_gcub1 = Button(win_g, text='Расчитать', command=G1cub1, cursor = 'hand1')
    but_gcub2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gcub1.grid(column=0, row=5)
    but_gcub2.grid(column=1, row=5, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G1pir():    
    win_g = Toplevel()
    win_g.title('Расчёт объёма пирамиды')
    win_g.geometry('500x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт объёма пирамиды'
    masf.append(s) 

    def G1pir1():
        if (ent_gpir1.get() == '') or (ent_gpir2.get() == ''):
            lab_gpir99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_gpir1.get().isdigit() and ent_gpir2.get().isdigit()) == False:
            lab_gpir99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gpir99.configure(text=str(1/3 * int(ent_gpir1.get())* int(ent_gpir2.get())), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт объёма пирамиды ' + '\n' + 'Высота = ' + ent_gpir1.get() + '\t' + 'Площадь основания = ' + ent_gpir2.get() + '\t' + '--> ' + str(1/3 * int(ent_gpir1.get())* int(ent_gpir2.get())) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_gpir99.configure(text='')
        ent_gpir1.delete(0, END)
        ent_gpir2.delete(0, END)

    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_gpir1 = Label(win_g, text='Введите высоту пирамиды:', padx = 3, pady = 2)
    lab_gpir2 = Label(win_g, text='Введите площадь основания пирамиды:', padx = 3, pady = 2)
    lab_gpir3 = Label(win_g, text='Ответ:', padx = 3)
    lab_gpir99 = Label(win_g, text='')
    lab_gpir1.grid(column=0, row=0, sticky=W)
    lab_gpir2.grid(column=0, row=1, sticky=W)
    lab_gpir3.grid(column=0, row=2, sticky=W)
    lab_gpir99.grid(column=1, row=2, sticky=W)
    
    global photo
    photo = tk.PhotoImage(file = './img/volume_piramida.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.2, rely=0.30)
    
    ent_gpir1 = Entry(win_g, width=10)
    ent_gpir2 = Entry(win_g, width=10)
    ent_gpir1.grid(column=1, row=0, sticky=W)
    ent_gpir2.grid(column=1, row=1, sticky=W)
    ent_gpir1.focus_set()

    but_gpir1 = Button(win_g, text='Расчитать', command=G1pir1, cursor = 'hand1')
    but_gpir2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gpir1.grid(column=0, row=5)
    but_gpir2.grid(column=1, row=5, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G1con():
    win_g = Toplevel()
    win_g.title('Расчёт объёма конуса')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт объёма конуса'
    masf.append(s) 

    def G1con1():
        if (ent_gcon1.get() == '') or (ent_gcon2.get() == ''):
            lab_gcon99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_gcon1.get().isdigit() and ent_gcon2.get().isdigit()) == False:
            lab_gcon99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gcon99.configure(text=str(1/3 * 3.14 * (int(ent_gcon1.get()) ** 2)* int(ent_gcon2.get())), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт объёма конуса ' + '\n' + 'Радиус = ' + ent_gcon1.get() + '\t' + 'Высота = ' + ent_gcon2.get() + '\t' + '--> ' + str(1/3 * 3.14 * (int(ent_gcon1.get()) ** 2)* int(ent_gcon2.get())) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_gcon99.configure(text='')
        ent_gcon1.delete(0, END)
        ent_gcon2.delete(0, END)

    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s)
        
    lab_gcon1 = Label(win_g, text='Введите радиус конуса:', padx = 3, pady = 2)
    lab_gcon2 = Label(win_g, text='Введите высоту конуса:', padx = 3, pady = 2)
    lab_gcon3 = Label(win_g, text='Ответ:', padx = 3, pady = 2)
    lab_gcon99 = Label(win_g, text='')
    lab_gcon1.grid(column=0, row=0, sticky=W)
    lab_gcon2.grid(column=0, row=1, sticky=W)
    lab_gcon3.grid(column=0, row=2, sticky=W)
    lab_gcon99.grid(column=1, row=2, sticky=W)

    ent_gcon1 = Entry(win_g, width=10)
    ent_gcon2 = Entry(win_g, width=10)
    ent_gcon1.grid(column=1, row=0, sticky=W)
    ent_gcon2.grid(column=1, row=1, sticky=W)
    ent_gcon1.focus_set()

    global photo
    photo = tk.PhotoImage(file = './img/volume_konus.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.35, rely=0.30)

    but_gcon1 = Button(win_g, text='Расчитать', command=G1con1, cursor = 'hand1')
    but_gcon2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gcon1.grid(column=0, row=5)
    but_gcon2.grid(column=1, row=5, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G1shil():
    win_g = Toplevel()
    win_g.title('Расчёт объёма цилиндра')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт объёма цилиндра'
    masf.append(s) 

    def G1shil1():
        if (ent_gshil1.get() == '') or (ent_gshil2.get() == ''):
            lab_gshil99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_gshil1.get().isdigit() and ent_gshil2.get().isdigit()) == False:
            lab_gshil99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gshil99.configure(text=str(3.14 * (int(ent_gshil1.get()) ** 2)* int(ent_gshil2.get())), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт объёма цилиндра ' + '\n' + 'Радиус = ' + ent_gshil1.get() + '\t' + 'Высота = ' + ent_gshil2.get() + '\t' + '--> ' + str(3.14 * (int(ent_gshil1.get()) ** 2)* int(ent_gshil2.get())) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_gshil99.configure(text='')
        ent_gshil1.delete(0, END)
        ent_gshil2.delete(0, END)

    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_gshil1 = Label(win_g, text='Введите радиус цилиндра:', padx = 3, pady = 3)
    lab_gshil2 = Label(win_g, text='Введите высоту цилиндра:', padx = 3, pady = 3)
    lab_gshil3 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_gshil99 = Label(win_g, text='')
    lab_gshil1.grid(column=0, row=0, sticky=W)
    lab_gshil2.grid(column=0, row=1, sticky=W)
    lab_gshil3.grid(column=0, row=2, sticky=W)
    lab_gshil99.grid(column=1, row=2, sticky=W)

    ent_gshil1 = Entry(win_g, width=10)
    ent_gshil2 = Entry(win_g, width=10)
    ent_gshil1.grid(column=1, row=0, sticky=W)
    ent_gshil2.grid(column=1, row=1, sticky=W)
    ent_gshil1.focus_set()
    
    global photo
    photo = tk.PhotoImage(file = './img/volume_cilindr.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.35, rely=0.30)

    but_gshil1 = Button(win_g, text='Расчитать', command=G1shil1, cursor = 'hand1')
    but_gshil2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gshil1.grid(column=0, row=5)
    but_gshil2.grid(column=1, row=5, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G1cr():
    win_g = Toplevel()
    win_g.title('Расчёт объёма шара')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт объёма шара'
    masf.append(s) 

    def G1cr1():
        if (ent_gcr1.get() == ''):
            lab_gcr99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_gcr1.get().isdigit()) == False:
            lab_gcr99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gcr99.configure(text=str(4 / 3 * 3.14 * (int(ent_gcr1.get()) ** 3)), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт объёма шара ' + '\n' + 'Радиус = ' + ent_gcr1.get() + '\t' + '--> ' + str(4 / 3 * 3.14 * (int(ent_gcr1.get()) ** 3)) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_gcr99.configure(text='')
        ent_gcr1.delete(0, END)
        
    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_gcr1 = Label(win_g, text='Введите радиус шара:', padx = 3, pady = 3) 
    lab_gcr2 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_gcr99 = Label(win_g, text='')
    lab_gcr1.grid(column=0, row=0, sticky=W)
    lab_gcr2.grid(column=0, row=1, sticky=W)
    lab_gcr99.grid(column=1, row=1, sticky=W)
    
    ent_gcr1 = Entry(win_g, width=10)
    ent_gcr1.grid(column=1, row=0, sticky=W)
    ent_gcr1.focus_set()   

    global photo
    photo = tk.PhotoImage(file = './img/volume_shar.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.22, rely=0.25)

    but_gcr1 = Button(win_g, text='Расчитать', command=G1cr1, cursor = 'hand1')
    but_gcr2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gcr1.grid(column=0, row=5)
    but_gcr2.grid(column=1, row=5, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G1pr():
    win_g = Toplevel()
    win_g.title('Расчёт объёма призмы')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт объёма призмы'
    masf.append(s) 

    def G1pr1():
        if (ent_gpr1.get() == '') or (ent_gpr2.get() == ''):
            lab_gpr99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_gpr1.get().isdigit() and ent_gpr2.get().isdigit()) == False:
            lab_gpr99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gpr99.configure(text=str(int(ent_gpr1.get()) * int(ent_gpr2.get())), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт объёма призмы ' + '\n' + 'Площадь основания = ' + ent_gpr1.get() + '\t' + 'Высота = ' + ent_gpr2.get() + '\t' + '--> ' + str(int(ent_gpr1.get()) * int(ent_gpr2.get())) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_gpr99.configure(text='')
        ent_gpr1.delete(0, END)
        ent_gpr2.delete(0, END)

    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_gpr1 = Label(win_g, text='Введите площадь основания призмы:', padx = 3, pady = 3)
    lab_gpr2 = Label(win_g, text='Введите высоту призмы:', padx = 3, pady = 3)
    lab_gpr3 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_gpr99 = Label(win_g, text='')
    lab_gpr1.grid(column=0, row=0, sticky=W)
    lab_gpr2.grid(column=0, row=1, sticky=W)
    lab_gpr3.grid(column=0, row=2, sticky=W)
    lab_gpr99.grid(column=1, row=2, sticky=W)

    ent_gpr1 = Entry(win_g, width=10)
    ent_gpr2 = Entry(win_g, width=10)
    ent_gpr1.grid(column=1, row=0, sticky=W)
    ent_gpr2.grid(column=1, row=1, sticky=W)
    ent_gpr1.focus_set()

    global photo
    photo = tk.PhotoImage(file = './img/volume_prizma.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.35, rely=0.33)

    but_gpr1 = Button(win_g, text='Расчитать', command=G1pr1, cursor = 'hand1')
    but_gpr2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gpr1.grid(column=0, row=5)
    but_gpr2.grid(column=1, row=5, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G2():
    rad_gd1.grid_remove()
    rad_gd2.grid_remove()
    rad_gd3.grid_remove()
    rad_gd4.grid_remove()
    rad_gd5.grid_remove()
    rad_gd6.grid_remove()
    rad_gd1a.grid_remove()
    rad_gd2a.grid_remove()
    rad_gd3a.grid_remove()
    rad_gd4a.grid_remove()
    rad_gd5a.grid_remove()
    rad_gd7.grid_remove()
    rad_gd7a.grid_remove()
    rad_gd8.grid_remove()
    rad_gd8a.grid_remove()
    rad_gd10.grid_remove()
    rad_gd10a.grid_remove()
    rad_gd11.grid_remove()
    rad_gd12.grid_remove()
    rad_gd13.grid_remove()
    rad_gd13a.grid_remove()
    rad_gd14.grid_remove()
    rad_gd15.grid_remove()
    rad_gd16.grid_remove()
    rad_gd1a.grid(column=0, row=12, sticky=W)
    rad_gd2a.grid(column=0, row=13, sticky=W)
    rad_gd3a.grid(column=0, row=14, sticky=W)
    rad_gd4a.grid(column=0, row=15, sticky=W)
    rad_gd5a.grid(column=0, row=16, sticky=W)
    lab3 = Label(win, text='Доп. выбор:', fg='black')
    lab3.grid(column=0, row=11, sticky=W)

def G1cuba():
    win_g = Toplevel()
    win_g.title('Расчёт площади поверхности куба')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт площади поверхности куба'
    masf.append(s) 

    def G1cuba1():
        if (ent_gcuba1.get() == ''):
            lab_gcuba3.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_gcuba1.get().isdigit()) == False:
            lab_gcuba3.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gcuba3.configure(text=str((6 * int(ent_gcuba1.get()) ** 2)), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт площади поверхности куба ' + '\n' + 'Сторона a = ' + ent_gcuba1.get() + '\t' + '--> ' + str((6 * int(ent_gcuba1.get()) ** 2)) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)        

    def Del():
        lab_gcuba3.configure(text='')
        ent_gcuba1.delete(0, END)

    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_gcuba1 = Label(win_g, text='Введите сторону куба(a):', padx = 3, pady = 3)
    lab_gcuba2 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_gcuba3 = Label(win_g, text='')
    lab_gcuba1.grid(column=0, row=0, sticky=W)
    lab_gcuba2.grid(column=0, row=1, sticky=W)
    lab_gcuba3.grid(column=1, row=1, sticky=W)

    ent_gcuba1 = Entry(win_g, width=10)
    ent_gcuba1.grid(column=1, row=0, sticky=W)
    ent_gcuba1.focus_set()

    global photo
    photo = tk.PhotoImage(file = './img/square_pov_cube.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.30, rely=0.30)

    but_gcuba1 = Button(win_g, text='Расчитать', command=G1cuba1, cursor = 'hand1')
    but_gcuba2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gcuba1.grid(column=0, row=100)
    but_gcuba2.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G1pira():
    win_g = Toplevel()
    win_g.title('Расчёт площади поверхности пирамиды')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт площади поверхности пирамиды'
    masf.append(s) 

    def G1pira1():
        if (ent_gpira1.get() == '') or (ent_gpira2.get() == '') or (ent_gpira3.get() == ''):
            lab_gpira99.configure(text='Введите данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_gpira1.get().isdigit() and ent_gpira2.get().isdigit() and ent_gpira3.get().isdigit()) == False:
            lab_gpira99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gpira99.configure(text=str((0.5 * int(ent_gpira1.get())) * int(ent_gpira2.get()) + int(ent_gpira3.get())), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт площади поверхности пирамиды ' + '\n' + 'Периметр основания = ' + ent_gpira1.get() + '\t' + 'Апофема = ' + ent_gpira2.get() + '\t' + 'Площадь основания = ' + ent_gpira3.get() + '\t' + '--> ' + str((0.5 * int(ent_gpira1.get())) * int(ent_gpira2.get()) + int(ent_gpira3.get())) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_gpira99.configure(text='')
        ent_gpira1.delete(0, END)
        ent_gpira2.delete(0, END)
        ent_gpira3.delete(0, END)

    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_gpira1 = Label(win_g, text='Введите периметр основания(P):', padx = 3, pady = 3)
    lab_gpira2 = Label(win_g, text='Введите апофему(L):', padx = 3, pady = 3)
    lab_gpira3 = Label(win_g, text='Площадь основания(S осн):', padx = 3, pady = 3)
    lab_gpira4 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_gpira99 = Label(win_g, text='')
    lab_gpira1.grid(column=0, row=0, sticky=W)
    lab_gpira2.grid(column=0, row=1, sticky=W)
    lab_gpira3.grid(column=0, row=2, sticky=W)
    lab_gpira4.grid(column=0, row=99, sticky=W)
    lab_gpira99.grid(column=1, row=99, sticky=W)

    ent_gpira1 = Entry(win_g, width=10)
    ent_gpira2 = Entry(win_g, width=10)
    ent_gpira3 = Entry(win_g, width=10)
    ent_gpira1.grid(column=1, row=0, sticky=W)
    ent_gpira2.grid(column=1, row=1, sticky=W)
    ent_gpira3.grid(column=1, row=2, sticky=W)
    ent_gpira1.focus_set()    
    
    global photo
    photo = tk.PhotoImage(file = './img/square_pov_piramida.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.25, rely=0.40)    
    
    but_gpira1 = Button(win_g, text='Расчитать', command=G1pira1, cursor = 'hand1')
    but_gpira2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gpira1.grid(column=0, row=100)
    but_gpira2.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G1cona():
    win_g = Toplevel()
    win_g.title('Расчёт площади поверхности конуса')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт площади поверхности конуса'
    masf.append(s) 

    def G1cona1():
        if (ent_gcona1.get() == '') or (ent_gcona2.get() == ''):
            lab_gcona99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_gcona1.get().isdigit() and ent_gcona2.get().isdigit()) == False:
            lab_gcona99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gcona99.configure(text=str(3.14 * int(ent_gcona1.get()) * (int(ent_gcona1.get()) + int(ent_gcona2.get()))), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт площади поверхности конуса ' + '\n' + 'Радиус = ' + ent_gcona1.get() + '\t' + 'Апофема = ' + ent_gcona2.get() + '\t' + '--> ' + str(3.14 * int(ent_gcona1.get()) * (int(ent_gcona1.get()) + int(ent_gcona2.get()))) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_gcona99.configure(text='')
        ent_gcona1.delete(0, END)
        ent_gcona2.delete(0, END)

    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_gcona1 = Label(win_g, text='Введите радиус основания конуса(r):', padx = 3, pady = 3)
    lab_gcona2 = Label(win_g, text='Введите апофему конуса(l):', padx = 3, pady = 3)
    lab_gcona4 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_gcona99 = Label(win_g, text='')
    lab_gcona1.grid(column=0, row=0, sticky=W)
    lab_gcona2.grid(column=0, row=1, sticky=W)
    lab_gcona4.grid(column=0, row=2, sticky=W)
    lab_gcona99.grid(column=1, row=2, sticky=W)

    ent_gcona1 = Entry(win_g, width=10)
    ent_gcona2 = Entry(win_g, width=10)
    ent_gcona1.grid(column=1, row=0, sticky=W)
    ent_gcona2.grid(column=1, row=1, sticky=W)
    ent_gcona1.focus_set() 

    global photo
    photo = tk.PhotoImage(file = './img/square_pov_konus.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.35, rely=0.32)

    but_gcona1 = Button(win_g, text='Расчитать', command=G1cona1, cursor = 'hand1')
    but_gcona2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gcona1.grid(column=0, row=100)
    but_gcona2.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G1shila():
    win_g = Toplevel()
    win_g.title('Расчёт площади поверхности цилиндра')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт площади поверхности цилиндра'
    masf.append(s) 

    def G1shila1():
        if (ent_gshila1.get() == '') or (ent_gshila2.get() == ''):
            lab_gshila99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_gshila1.get().isdigit() and ent_gshila2.get().isdigit()) == False:
            lab_gshila99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gshila99.configure(text=str((2 * 3.14 * int(ent_gshila1.get()) * int(ent_gshila2.get())) + (2 * 3.14 * (int(ent_gshila1.get()))**2)), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт площади поверхности цилиндра ' + '\n' + 'Радиус = ' + ent_gshila1.get() + '\t' + 'Высота = ' + ent_gshila2.get() + '\t' + '--> ' + str((2 * 3.14 * int(ent_gshila1.get()) * int(ent_gshila2.get())) + (2 * 3.14 * (int(ent_gshila1.get()))**2)) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_gshila99.configure(text='')
        ent_gshila1.delete(0, END)
        ent_gshila2.delete(0, END)

    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_gshila1 = Label(win_g, text='Введите радиус цилиндра(R):', padx = 3, pady = 3)
    lab_gshila2 = Label(win_g, text='Введите высоту цилиндра(H):', padx = 3, pady = 3)
    lab_gshila3 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_gshila99 = Label(win_g, text='')
    lab_gshila1.grid(column=0, row=0, sticky=W)
    lab_gshila2.grid(column=0, row=1, sticky=W)
    lab_gshila3.grid(column=0, row=2, sticky=W)
    lab_gshila99.grid(column=1, row=2, sticky=W)

    ent_gshila1 = Entry(win_g, width=10)
    ent_gshila2 = Entry(win_g, width=10)
    ent_gshila1.grid(column=1, row=0, sticky=W)
    ent_gshila2.grid(column=1, row=1, sticky=W)
    ent_gshila1.focus_set() 

    global photo
    photo = tk.PhotoImage(file = './img/volume_konus.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.35, rely=0.30)

    but_gshila1 = Button(win_g, text='Расчитать', command=G1shila1, cursor = 'hand1')
    but_gshila2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gshila1.grid(column=0, row=100)
    but_gshila2.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G1cra():
    win_g = Toplevel()
    win_g.title('Расчёт площади поверхности шара')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт площади поверхности шара'
    masf.append(s) 

    def G1cra1():
        if (ent_gcra1.get() == ''):
            lab_gcra99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_gcra1.get().isdigit()) == False:
            lab_gcra99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gcra99.configure(text=str(4 * 3.14 * (int(ent_gcra1.get()) ** 2)), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт площади поверхности шара ' + '\n' + 'Радиус = ' + ent_gcra1.get() + '\t' + '--> ' + str(4 * 3.14 * (int(ent_gcra1.get()) ** 2)) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_gcra99.configure(text='')
        ent_gcra1.delete(0, END)
        
    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_gcra1 = Label(win_g, text='Введите радиус шара(R):', padx = 3, pady = 3) 
    lab_gcra2 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_gcra99 = Label(win_g, text='')
    lab_gcra1.grid(column=0, row=0, sticky=W)
    lab_gcra2.grid(column=0, row=1, sticky=W)
    lab_gcra99.grid(column=1, row=1, sticky=W)
    

    ent_gcra1 = Entry(win_g, width=10)
    ent_gcra1.grid(column=1, row=0, sticky=W)
    ent_gcra1.focus_set()   

    global photo
    photo = tk.PhotoImage(file = './img/volume_shar.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.23, rely=0.25)

    but_gcra1 = Button(win_g, text='Расчитать', command=G1cra1, cursor = 'hand1')
    but_gcra2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gcra1.grid(column=0, row=100)
    but_gcra2.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G3():
    rad_gd1.grid_remove()
    rad_gd2.grid_remove()
    rad_gd3.grid_remove()
    rad_gd4.grid_remove()
    rad_gd5.grid_remove()
    rad_gd6.grid_remove()
    rad_gd1a.grid_remove()
    rad_gd2a.grid_remove()
    rad_gd3a.grid_remove()
    rad_gd4a.grid_remove()
    rad_gd5a.grid_remove()
    rad_gd7.grid_remove()
    rad_gd7a.grid_remove()
    rad_gd8.grid_remove()
    rad_gd8a.grid_remove()
    rad_gd10.grid_remove()
    rad_gd10a.grid_remove()
    rad_gd11.grid_remove()
    rad_gd12.grid_remove()
    rad_gd13.grid_remove()
    rad_gd13a.grid_remove()
    rad_gd14.grid_remove()
    rad_gd15.grid_remove()
    rad_gd16.grid_remove()
    rad_gd7.grid(column=0, row=18, sticky=W)
    rad_gd8.grid(column=0, row=19, sticky=W)
    rad_gd10.grid(column=0, row=21, sticky=W)
    rad_gd11.grid(column=0, row=22, sticky=W)
    rad_gd12.grid(column=0, row=23, sticky=W)
    rad_gd13.grid(column=0, row=24, sticky=W)
    lab3 = Label(win, text='Доп. выбор:', fg='black')
    lab3.grid(column=0, row=11, sticky=W)


def G3cv():
    win_g = Toplevel()
    win_g.title('Расчёт площади квадрата')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт площади квадрата'
    masf.append(s) 

    def G3cv1():
        if (ent_gcv1.get() == ''):
            lab_gcv99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_gcv1.get().isdigit()) == False:
            lab_gcv99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)           
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gcv99.configure(text=str(int(ent_gcv1.get()) ** 2), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт площади квадрата ' + '\n' + 'Сторона a = ' + ent_gcv1.get() + '\t' + '--> ' + str(int(ent_gcv1.get()) ** 2) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_gcv99.configure(text='')
        ent_gcv1.delete(0, END)
        
    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_gcv1 = Label(win_g, text='Введите сторону квадрата(a):', padx = 3, pady = 3) 
    lab_gcv98 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_gcv99 = Label(win_g, text='')
    lab_gcv1.grid(column=0, row=0, sticky=W)
    lab_gcv98.grid(column=0, row=1, sticky=W)
    lab_gcv99.grid(column=1, row=1, sticky=W)
    

    ent_gcv1 = Entry(win_g, width=10)
    ent_gcv1.grid(column=1, row=0, sticky=W)
    ent_gcv1.focus_set()   

    global photo
    photo = tk.PhotoImage(file = './img/square_kvadrat.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.30, rely=0.35)

    but_gcv1 = Button(win_g, text='Расчитать', command=G3cv1, cursor = 'hand1')
    but_gcv2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gcv1.grid(column=0, row=5)
    but_gcv2.grid(column=1, row=5, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G3pram():
    win_g = Toplevel()
    win_g.title('Расчёт площади прямоугольника')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт площади прямоугольника'
    masf.append(s) 

    def G3pram1():
        if (ent_gpram1.get() == '') or (ent_gpram2.get() == ''):
            lab_gpram99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_gpram1.get().isdigit() and ent_gpram2.get().isdigit()) == False:
            lab_gpram99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gpram99.configure(text=str(int(ent_gpram1.get()) * int(ent_gpram2.get())), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт площади прямоугольника ' + '\n' + 'Cторона a = ' + ent_gpram1.get() + '\t' + 'Cторона b = ' + ent_gpram2.get() + '\t' + '--> ' + str(int(ent_gpram1.get()) * int(ent_gpram2.get())) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_gpram99.configure(text='')
        ent_gpram1.delete(0, END)
        ent_gpram2.delete(0, END)
        
    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_gpram1 = Label(win_g, text='Введите сторону прямоугольника(a):', padx = 3, pady = 3)
    lab_gpram2 = Label(win_g, text='Введите сторону прямоугольника(b):', padx = 3, pady = 3)
    lab_gpram98 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_gpram99 = Label(win_g, text='')
    lab_gpram1.grid(column=0, row=0, sticky=W)
    lab_gpram2.grid(column=0, row=1, sticky=W)
    lab_gpram98.grid(column=0, row=99, sticky=W)
    lab_gpram99.grid(column=1, row=99, sticky=W)
    

    ent_gpram1 = Entry(win_g, width=10)
    ent_gpram2 = Entry(win_g, width=10)
    ent_gpram1.grid(column=1, row=0, sticky=W)
    ent_gpram2.grid(column=1, row=1, sticky=W)
    ent_gpram1.focus_set()   

    global photo
    photo = tk.PhotoImage(file = './img/square_pryam.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.25, rely=0.40)

    but_gpram1 = Button(win_g, text='Расчитать', command=G3pram1, cursor = 'hand1')
    but_gpram2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gpram1.grid(column=0, row=100)
    but_gpram2.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G3tr():
    win_g = Toplevel()
    win_g.title('Расчёт площади треугольника')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт площади треугольника'
    masf.append(s) 

    def G3tr1():
        if (ent_gtr1.get() == '') or (ent_gtr2.get() == ''):
            lab_gtr99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_gtr1.get().isdigit() and ent_gtr2.get().isdigit()) == False:
            lab_gtr99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gtr99.configure(text=str((int(ent_gtr1.get()) * int(ent_gtr2.get())) / 2), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт площади треугольника ' + '\n' + 'Основание = ' + ent_gtr1.get() + '\t' + 'Высота = ' + ent_gtr2.get() + '\t' + '--> ' + str((int(ent_gtr1.get()) * int(ent_gtr2.get())) / 2) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_gtr99.configure(text='')
        ent_gtr1.delete(0, END)
        ent_gtr2.delete(0, END)
        
    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_gtr1 = Label(win_g, text='Введите сторону основания треугольника(a):', padx = 3, pady = 3)
    lab_gtr2 = Label(win_g, text='Введите высоту треугольника(h):', padx = 3, pady = 3)
    lab_gtr98 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_gtr99 = Label(win_g, text='')
    lab_gtr1.grid(column=0, row=0, sticky=W)
    lab_gtr2.grid(column=0, row=1, sticky=W)
    lab_gtr98.grid(column=0, row=99, sticky=W)
    lab_gtr99.grid(column=1, row=99, sticky=W)
    

    ent_gtr1 = Entry(win_g, width=10)
    ent_gtr2 = Entry(win_g, width=10)
    ent_gtr1.grid(column=1, row=0, sticky=W)
    ent_gtr2.grid(column=1, row=1, sticky=W)
    ent_gtr1.focus_set()   

    global photo
    photo = tk.PhotoImage(file = './img/square_treyg.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.30, rely=0.35)

    but_gtr1 = Button(win_g, text='Расчитать', command=G3tr1, cursor = 'hand1')
    but_gtr2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gtr1.grid(column=0, row=100)
    but_gtr2.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G3trap():
    win_g = Toplevel()
    win_g.title('Расчёт площади трапеции')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт площади трапеции'
    masf.append(s) 

    def G3trap1():
        if (ent_gtrap1.get() == '') or (ent_gtrap2.get() == '') or (ent_gtrap3.get() == ''):
            lab_gtrap99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_gtrap1.get().isdigit() and ent_gtrap2.get().isdigit() and ent_gtrap3.get().isdigit()) == False:
            lab_gtrap99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gtrap99.configure(text=str(((int(ent_gtrap1.get()) + int(ent_gtrap2.get())) / 2) * int(ent_gtrap3.get())), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт площади трапеции ' + '\n' + 'Основание 1 = ' + ent_gtrap1.get() + '\t' + 'Основание 2 = ' + ent_gtrap2.get() + '\t' +  'Высота = ' + ent_gtrap3.get() + '\t' + '--> ' + str(((int(ent_gtrap1.get()) + int(ent_gtrap2.get())) / 2) * int(ent_gtrap3.get())) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_gtrap99.configure(text='')
        ent_gtrap1.delete(0, END)
        ent_gtrap2.delete(0, END)
        ent_gtrap3.delete(0, END)
        
    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_gtrap1 = Label(win_g, text='Введите первое основания трапеции(a):', padx = 3, pady = 3)
    lab_gtrap2 = Label(win_g, text='Введите второе основание трапеции(b):', padx = 3, pady = 3)
    lab_gtrap3 = Label(win_g, text='Введите высоту трапеции(h):', padx = 3, pady = 3)
    lab_gtrap98 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_gtrap99 = Label(win_g, text='')
    lab_gtrap1.grid(column=0, row=0, sticky=W)
    lab_gtrap2.grid(column=0, row=1, sticky=W)
    lab_gtrap3.grid(column=0, row=2, sticky=W)
    lab_gtrap98.grid(column=0, row=99, sticky=W)
    lab_gtrap99.grid(column=1, row=99, sticky=W)

    ent_gtrap1 = Entry(win_g, width=10)
    ent_gtrap2 = Entry(win_g, width=10)
    ent_gtrap3 = Entry(win_g, width=10)
    ent_gtrap1.grid(column=1, row=0, sticky=W)
    ent_gtrap2.grid(column=1, row=1, sticky=W)
    ent_gtrap3.grid(column=1, row=2, sticky=W)
    ent_gtrap1.focus_set()   

    global photo
    photo = tk.PhotoImage(file = './img/square_trapesia.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.28, rely=0.45)

    but_gtrap1 = Button(win_g, text='Расчитать', command=G3trap1, cursor = 'hand1')
    but_gtrap2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gtrap1.grid(column=0, row=100)
    but_gtrap2.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G3romb():
    win_g = Toplevel()
    win_g.title('Расчёт площади ромба')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт площади ромба'
    masf.append(s) 

    def G3romb1():
        if (ent_gromb1.get() == '') or (ent_gromb2.get() == ''):
            lab_gromb99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_gromb1.get().isdigit() and ent_gromb2.get().isdigit()) == False:
            lab_gromb99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gromb99.configure(text=str(int(ent_gromb1.get()) * int(ent_gromb2.get())), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт площади ромба ' + '\n' + 'Сторона a = ' + ent_gromb1.get() + '\t' + 'Высота = ' + ent_gromb2.get() + '\t' + '--> ' + str(int(ent_gromb1.get()) * int(ent_gromb2.get())) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_gromb99.configure(text='')
        ent_gromb1.delete(0, END)
        ent_gromb2.delete(0, END)
        
    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_gromb1 = Label(win_g, text='Введите сторону ромба(a):', padx = 3, pady = 3)
    lab_gromb2 = Label(win_g, text='Введите высоту ромба(h):', padx = 3, pady = 3)
    lab_gromb98 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_gromb99 = Label(win_g, text='')
    lab_gromb1.grid(column=0, row=0, sticky=W)
    lab_gromb2.grid(column=0, row=1, sticky=W)
    lab_gromb98.grid(column=0, row=99, sticky=W)
    lab_gromb99.grid(column=1, row=99, sticky=W)
    
    ent_gromb1 = Entry(win_g, width=10)
    ent_gromb2 = Entry(win_g, width=10)
    ent_gromb1.grid(column=1, row=0, sticky=W)
    ent_gromb2.grid(column=1, row=1, sticky=W)
    ent_gromb1.focus_set()   

    global photo
    photo = tk.PhotoImage(file = './img/square_romb.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.35, rely=0.35)

    but_gromb1 = Button(win_g, text='Расчитать', command=G3romb1, cursor = 'hand1')
    but_gromb2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gromb1.grid(column=0, row=100)
    but_gromb2.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G3crug():
    win_g = Toplevel()
    win_g.title('Расчёт площади круга')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт площади круга'
    masf.append(s) 

    def G3crug1():
        if (ent_gcrug1.get() == ''):
            lab_gcrug99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_gcrug1.get().isdigit()) == False:
            lab_gcrug99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gcrug99.configure(text=str(3.14 * (int(ent_gcrug1.get()) ** 2)), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт площади круга ' + '\n' + 'Радиус = ' + ent_gcrug1.get() + '\t' + '--> ' + str(3.14 * (int(ent_gcrug1.get()) ** 2)) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)        

    def Del():
        lab_gcrug99.configure(text='')
        ent_gcrug1.delete(0, END)
        
    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s)         

    lab_gcrug1 = Label(win_g, text='Введите радиус круга:', padx = 3, pady = 3) 
    lab_gcrug98 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_gcrug99 = Label(win_g, text='')
    lab_gcrug1.grid(column=0, row=0, sticky=W)
    lab_gcrug98.grid(column=0, row=99, sticky=W)
    lab_gcrug99.grid(column=1, row=99, sticky=W)
    
    ent_gcrug1 = Entry(win_g, width=10)
    ent_gcrug1.grid(column=1, row=0, sticky=W)
    ent_gcrug1.focus_set()   

    global photo
    photo = tk.PhotoImage(file = './img/square_kruga.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.35, rely=0.35)

    but_gcrug1 = Button(win_g, text='Расчитать', command=G3crug1, cursor = 'hand1')
    but_gcrug2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gcrug1.grid(column=0, row=100)
    but_gcrug2.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G4():
    rad_gd1.grid_remove()
    rad_gd2.grid_remove()
    rad_gd3.grid_remove()
    rad_gd4.grid_remove()
    rad_gd5.grid_remove()
    rad_gd6.grid_remove()
    rad_gd1a.grid_remove()
    rad_gd2a.grid_remove()
    rad_gd3a.grid_remove()
    rad_gd4a.grid_remove()
    rad_gd5a.grid_remove()
    rad_gd7.grid_remove()
    rad_gd7a.grid_remove()
    rad_gd8.grid_remove()
    rad_gd8a.grid_remove()
    rad_gd10.grid_remove()
    rad_gd10a.grid_remove()
    rad_gd11.grid_remove()
    rad_gd12.grid_remove()
    rad_gd13.grid_remove()
    rad_gd13a.grid_remove()
    rad_gd14.grid_remove()
    rad_gd15.grid_remove()
    rad_gd16.grid_remove()
    rad_gd7a.grid(column=0, row=19, sticky=W)
    rad_gd8a.grid(column=0, row=20, sticky=W)
    rad_gd10a.grid(column=0, row=21, sticky=W)
    rad_gd13a.grid(column=0, row=24, sticky=W)
    lab3 = Label(win, text='Доп. выбор:', fg='black')
    lab3.grid(column=0, row=11, sticky=W)

def G3cva():
    win_g = Toplevel()
    win_g.title('Расчёт периметра квадрата')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт периметра квадрата'
    masf.append(s) 

    def G3cv1():
        if (ent_gcv1.get() == ''):
            lab_gcv99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_gcv1.get().isdigit()) == False:
            lab_gcv99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gcv99.configure(text=str(int(ent_gcv1.get()) * 4), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт периметра квадрата ' + '\n' + 'Сторона a = ' + ent_gcv1.get() + '\t' + '--> ' + str(int(ent_gcv1.get()) * 4) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_gcv99.configure(text='')
        ent_gcv1.delete(0, END)

    def closing():
        radio_var2.set(-1)
        win_g.destroy()    
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_gcv1 = Label(win_g, text='Введите сторону квадрата(a):', padx = 3, pady = 3) 
    lab_gcv98 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_gcv99 = Label(win_g, text='')
    lab_gcv1.grid(column=0, row=0, sticky=W)
    lab_gcv98.grid(column=0, row=99, sticky=W)
    lab_gcv99.grid(column=1, row=99, sticky=W)
    

    ent_gcv1 = Entry(win_g, width=10)
    ent_gcv1.grid(column=1, row=0, sticky=W)
    ent_gcv1.focus_set()   

    global photo
    photo = tk.PhotoImage(file = './img/perim_kvadrat.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.30, rely=0.30)

    but_gcv1 = Button(win_g, text='Расчитать', command=G3cv1, cursor = 'hand1')
    but_gcv2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gcv1.grid(column=0, row=100)
    but_gcv2.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G3prama():
    win_g = Toplevel()
    win_g.title('Расчёт периметра прямоугольника')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт периметра прямоугольника'
    masf.append(s) 

    def G3pram1():
        if (ent_gpram1.get() == '') or (ent_gpram2.get() == ''):
            lab_gpram99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_gpram1.get().isdigit() and ent_gpram2.get().isdigit()) == False:
            lab_gpram99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gpram99.configure(text=str(2 * (int(ent_gpram1.get()) + int(ent_gpram2.get()))), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт периметра прямоугольника ' + '\n' + 'Сторона a = ' + ent_gpram1.get() + '\t' + 'Сторона b = ' + ent_gpram2.get() + '\t' + '--> ' + str(2 * (int(ent_gpram1.get()) + int(ent_gpram2.get()))) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_gpram99.configure(text='')
        ent_gpram1.delete(0, END)
        ent_gpram2.delete(0, END)
        
    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_gpram1 = Label(win_g, text='Введите сторону прямоугольника(a):', padx = 3, pady = 3)
    lab_gpram2 = Label(win_g, text='Введите сторону прямоугольника(b):', padx = 3, pady = 3)
    lab_gpram98 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_gpram99 = Label(win_g, text='')
    lab_gpram1.grid(column=0, row=0, sticky=W)
    lab_gpram2.grid(column=0, row=1, sticky=W)
    lab_gpram98.grid(column=0, row=99, sticky=W)
    lab_gpram99.grid(column=1, row=99, sticky=W)

    ent_gpram1 = Entry(win_g, width=10)
    ent_gpram2 = Entry(win_g, width=10)
    ent_gpram1.grid(column=1, row=0, sticky=W)
    ent_gpram2.grid(column=1, row=1, sticky=W)
    ent_gpram1.focus_set()   

    global photo
    photo = tk.PhotoImage(file = './img/perim_pryam.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.18, rely=0.35)

    but_gpram1 = Button(win_g, text='Расчитать', command=G3pram1, cursor = 'hand1')
    but_gpram2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gpram1.grid(column=0, row=100)
    but_gpram2.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G3tra():
    win_g = Toplevel()
    win_g.title('Расчёт периметра треугольника')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт периметра треугольника'
    masf.append(s) 

    def G3tr1():
        if (ent_gtr1.get() == '') or (ent_gtr2.get() == '') or (ent_gtr3.get() == ''):
            lab_gtr99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_gtr1.get().isdigit() and ent_gtr2.get().isdigit() and ent_gtr3.get().isdigit()) == False:
            lab_gtr99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:            
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gtr99.configure(text=str(int(ent_gtr1.get()) + int(ent_gtr2.get()) + int(ent_gtr3.get())), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт периметра треугольника ' + '\n' + 'Сторона a = ' + ent_gtr1.get() + '\t' + 'Сторона b = ' + ent_gtr2.get() + '\t' + 'Сторона c = ' + ent_gtr3.get() + '\t' + '--> ' + str(int(ent_gtr1.get()) + int(ent_gtr2.get()) + int(ent_gtr3.get())) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_gtr99.configure(text='')
        ent_gtr1.delete(0, END)
        ent_gtr2.delete(0, END)
        ent_gtr3.delete(0, END)
        
    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_gtr1 = Label(win_g, text='Введите сторону треугольника:(a)', padx = 3, pady = 3)
    lab_gtr2 = Label(win_g, text='Введите сторону треугольника(b):', padx = 3, pady = 3)
    lab_gtr3 = Label(win_g, text='Введите сторону треугольника(c):', padx = 3, pady = 3)
    lab_gtr98 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_gtr99 = Label(win_g, text='')
    lab_gtr1.grid(column=0, row=0, sticky=W)
    lab_gtr2.grid(column=0, row=1, sticky=W)
    lab_gtr3.grid(column=0, row=2, sticky=W)
    lab_gtr98.grid(column=0, row=99, sticky=W)
    lab_gtr99.grid(column=1, row=99, sticky=W)

    ent_gtr1 = Entry(win_g, width=10)
    ent_gtr2 = Entry(win_g, width=10)
    ent_gtr3 = Entry(win_g, width=10)
    ent_gtr1.grid(column=1, row=0, sticky=W)
    ent_gtr2.grid(column=1, row=1, sticky=W)
    ent_gtr3.grid(column=1, row=2, sticky=W)
    ent_gtr1.focus_set()   

    global photo
    photo = tk.PhotoImage(file = './img/perim_treyg.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.33, rely=0.40)

    but_gtr1 = Button(win_g, text='Расчитать', command=G3tr1, cursor = 'hand1')
    but_gtr2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gtr1.grid(column=0, row=100)
    but_gtr2.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G3cruga():
    win_g = Toplevel()
    win_g.title('Расчёт периметра круга')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт периметра круга'
    masf.append(s) 

    def G3crug1():
        if (ent_gcrug1.get() == ''):
            lab_gcrug99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
        elif (ent_gcrug1.get().isdigit()) == False:
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
            lab_gcrug99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_gcrug99.configure(text=str(3.14 * (int(ent_gcrug1.get()) * 2)), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт периметра круга ' + '\n' + 'Радиус = ' + ent_gcrug1.get() + '\t' + '--> ' + str(3.14 * (int(ent_gcrug1.get()) * 2)) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_gcrug99.configure(text='')
        ent_gcrug1.delete(0, END)
        
    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s)        

    lab_gcrug1 = Label(win_g, text='Введите радиус круга:', padx = 3, pady = 3) 
    lab_gcrug98 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_gcrug99 = Label(win_g, text='')
    lab_gcrug1.grid(column=0, row=0, sticky=W)
    lab_gcrug98.grid(column=0, row=99, sticky=W)
    lab_gcrug99.grid(column=1, row=99, sticky=W)

    ent_gcrug1 = Entry(win_g, width=10)
    ent_gcrug1.grid(column=1, row=0, sticky=W)
    ent_gcrug1.focus_set()   

    global photo
    photo = tk.PhotoImage(file = './img/square_kruga.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.35, rely=0.30)

    but_gcrug1 = Button(win_g, text='Расчитать', command=G3crug1, cursor = 'hand1')
    but_gcrug2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_gcrug1.grid(column=0, row=100)
    but_gcrug2.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G5():
    rad_gd1.grid_remove()
    rad_gd2.grid_remove()
    rad_gd3.grid_remove()
    rad_gd4.grid_remove()
    rad_gd5.grid_remove()
    rad_gd6.grid_remove()
    rad_gd1a.grid_remove()
    rad_gd2a.grid_remove()
    rad_gd3a.grid_remove()
    rad_gd4a.grid_remove()
    rad_gd5a.grid_remove()
    rad_gd7.grid_remove()
    rad_gd7a.grid_remove()
    rad_gd8.grid_remove()
    rad_gd8a.grid_remove()
    rad_gd10.grid_remove()
    rad_gd10a.grid_remove()
    rad_gd11.grid_remove()
    rad_gd12.grid_remove()
    rad_gd13.grid_remove()
    rad_gd13a.grid_remove()
    rad_gd14.grid_remove()
    rad_gd15.grid_remove()
    rad_gd16.grid_remove()
    rad_gd14.grid(column=0, row=25, sticky=W)
    rad_gd15.grid(column=0, row=26, sticky=W)
    rad_gd16.grid(column=0, row=27, sticky=W)
    lab3 = Label(win, text='Доп. выбор:', fg='black')
    lab3.grid(column=0, row=11, sticky=W)

def G51():
    win_g = Toplevel()
    win_g.title('Расчёт расстояния между двумя точками 1-ная система')
    win_g.geometry('450x350')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт расстояния между двумя точками 1-ная система'
    masf.append(s) 

    def G51():
        if (ent_g51.get() == '') or (ent_g52.get() == ''):
            lab_g599.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        #elif (ent_g51.get().isdigit() and ent_g52.get().isdigit()) == False:
            #lab_g599.configure(text='Введите корректные данные', fg = 'red')
           # now = datetime.datetime.now()   
           # s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
           # masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_g599.configure(text=str(abs(int(ent_g51.get()) - int(ent_g52.get()))), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт расстояния между двумя точками 1-ная система ' + '\n' + 'x1 = ' + ent_g51.get() + '\t' + 'x2 = ' + ent_g52.get() + '\t' + '--> ' + str(abs(int(ent_g51.get()) - int(ent_g52.get()))) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_g599.configure(text='')
        ent_g51.delete(0, END)
        ent_g52.delete(0, END)

    def closing():
        radio_var2.set(-1)
        win_g.destroy()

    lab_g51 = Label(win_g, text='Введите координату x1:', padx = 3, pady = 3)
    lab_g52 = Label(win_g, text='Введите координату x2:', padx = 3, pady = 3)
    lab_g598 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_g599 = Label(win_g, text='')
    lab_g51.grid(column=0, row=0, sticky=W)
    lab_g52.grid(column=0, row=1, sticky=W)
    lab_g598.grid(column=0, row=99, sticky=W)
    lab_g599.grid(column=1, row=99, sticky=W)  

    ent_g51 = Entry(win_g, width=10)
    ent_g52 = Entry(win_g, width=10)
    ent_g51.grid(column=1, row=0, sticky=W)
    ent_g52.grid(column=1, row=1, sticky=W)
    ent_g51.focus_set()    

    global photo
    photo = tk.PhotoImage(file = './img/odnomer.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.28, rely=0.50)

    but_g51 = Button(win_g, text='Расчитать', command=G51, cursor = 'hand1')
    but_g52 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_g51.grid(column=0, row=100)
    but_g52.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G52():
    win_g = Toplevel()
    win_g.title('Расчёт расстояния между двумя точками 2-ная система')
    win_g.geometry('450x450')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт расстояния между двумя точками 2-ная система'
    masf.append(s) 

    def G51():
        if (ent_g51.get() == '') or (ent_g52.get() == '') or (ent_g53.get() == '') or (ent_g54.get() == ''):
            lab_g599.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
       # elif (ent_g51.get().isdigit() and ent_g52.get().isdigit() and ent_g53.get().isdigit() and ent_g54.get().isdigit()) == False:
          #  lab_g599.configure(text='Введите корректные данные', fg = 'red')
           # now = datetime.datetime.now()   
           # s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
           # masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_g599.configure(text=str(((((int(ent_g51.get()) - int(ent_g53.get())) ** 2) + ((int(ent_g52.get()) - int(ent_g54.get())) ** 2)) ** 0.5)), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт расстояния между двумя точками 2-ная система ' + '\n' + 'x1 = ' + ent_g51.get() + '\t' + 'y1 = ' + ent_g52.get() + '\t' + 'x2 = ' + ent_g53.get() + '\t' + 'y2 = '+ ent_g54.get() + '\t' + '--> ' + str(((((int(ent_g51.get()) - int(ent_g53.get())) ** 2) + ((int(ent_g52.get()) - int(ent_g54.get())) ** 2)) ** 0.5)) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_g599.configure(text='')
        ent_g51.delete(0, END)
        ent_g52.delete(0, END)
        ent_g53.delete(0, END)
        ent_g54.delete(0, END)

    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_g51 = Label(win_g, text='Введите координату x1:', padx = 3, pady = 3)
    lab_g52 = Label(win_g, text='Введите координату y1:', padx = 3, pady = 3)
    lab_g53 = Label(win_g, text='Введите координату x2:', padx = 3, pady = 3)
    lab_g54 = Label(win_g, text='Введите координату y2:', padx = 3, pady = 3)
    lab_g598 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_g599 = Label(win_g, text='')
    lab_g51.grid(column=0, row=0, sticky=W)
    lab_g52.grid(column=0, row=1, sticky=W)
    lab_g53.grid(column=0, row=2, sticky=W)
    lab_g54.grid(column=0, row=3, sticky=W)
    lab_g598.grid(column=0, row=99, sticky=W)
    lab_g599.grid(column=1, row=99, sticky=W)

    ent_g51 = Entry(win_g, width=10)
    ent_g52 = Entry(win_g, width=10)
    ent_g53 = Entry(win_g, width=10)
    ent_g54 = Entry(win_g, width=10)
    ent_g51.grid(column=1, row=0, sticky=W)
    ent_g52.grid(column=1, row=1, sticky=W)
    ent_g53.grid(column=1, row=2, sticky=W)
    ent_g54.grid(column=1, row=3, sticky=W)
    ent_g51.focus_set()    

    global photo
    photo = tk.PhotoImage(file = './img/dvymer.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.15, rely=0.36)

    but_g51 = Button(win_g, text='Расчитать', command=G51, cursor = 'hand1')
    but_g52 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_g51.grid(column=0, row=100)
    but_g52.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def G53():
    win_g = Toplevel()
    win_g.title('Расчёт расстояния между двумя точками 3-ная система')
    win_g.geometry('450x450')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Геометрии. Расчёт расстояния между двумя точками 3-ная система'
    masf.append(s) 

    def G51():
        if (ent_g51.get() == '') or (ent_g52.get() == '') or (ent_g53.get() == '') or (ent_g54.get() == '') or (ent_g55.get() == '') or (ent_g56.get() == ''):
            lab_g599.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
       # elif (ent_g51.get().isdigit() and ent_g52.get().isdigit() and ent_g53.get().isdigit() and ent_g54.get().isdigit() and ent_g55.get().isdigit() and ent_g56.get().isdigit()) == False:
          #  lab_g599.configure(text='Введите корректные данные', fg = 'red')
           # now = datetime.datetime.now()   
            #s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            #masf.append(s)            
        else:
            global count
            global k_math
            count += 1
            k_math += 1
            lab_g599.configure(text=str((((int(ent_g51.get()) - int(ent_g54.get())) ** 2) + ((int(ent_g52.get()) - int(ent_g55.get())) ** 2) + ((int(ent_g53.get()) - int(ent_g56.get())) ** 2))** 0.5), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт расстояния между двумя точками 3-ная система ' + '\n' + 'x1 = ' + ent_g51.get() + '\t' + 'y1 = ' + ent_g52.get() + '\t' + 'z1 = ' + ent_g53.get() + '\t' + 'x2 = ' + ent_g54.get() + '\t' + 'y2 = '+ ent_g55.get() + '\t' + 'z2 = ' + ent_g56.get() + '\t' + '--> ' + str((((int(ent_g51.get()) - int(ent_g54.get())) ** 2) + ((int(ent_g52.get()) - int(ent_g55.get())) ** 2) + ((int(ent_g53.get()) - int(ent_g56.get())) ** 2))** 0.5) + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Геометрии'
            masf.append(s)

    def Del():
        lab_g599.configure(text='')
        ent_g51.delete(0, END)
        ent_g52.delete(0, END)
        ent_g53.delete(0, END)
        ent_g54.delete(0, END)
        ent_g55.delete(0, END)
        ent_g56.delete(0, END)
        
    def closing():
        radio_var2.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_g51 = Label(win_g, text='Введите координату x1:', padx = 3, pady = 3)
    lab_g52 = Label(win_g, text='Введите координату y1:', padx = 3, pady = 3)
    lab_g53 = Label(win_g, text='Введите координату z1:', padx = 3, pady = 3)
    lab_g54 = Label(win_g, text='Введите координату x2:', padx = 3, pady = 3)
    lab_g55 = Label(win_g, text='Введите координату y2:', padx = 3, pady = 3)
    lab_g56 = Label(win_g, text='Введите координату z2:', padx = 3, pady = 3)
    lab_g598 = Label(win_g, text='Ответ:', padx = 3, pady = 3)
    lab_g599 = Label(win_g, text='')
    lab_g51.grid(column=0, row=0, sticky=W)
    lab_g52.grid(column=0, row=1, sticky=W)
    lab_g53.grid(column=0, row=2, sticky=W)
    lab_g54.grid(column=0, row=3, sticky=W)
    lab_g55.grid(column=0, row=4, sticky=W)
    lab_g56.grid(column=0, row=5, sticky=W)
    lab_g598.grid(column=0, row=99, sticky=W)
    lab_g599.grid(column=1, row=99, sticky=W)   

    ent_g51 = Entry(win_g, width=10)
    ent_g52 = Entry(win_g, width=10)
    ent_g53 = Entry(win_g, width=10)
    ent_g54 = Entry(win_g, width=10)
    ent_g55 = Entry(win_g, width=10)
    ent_g56 = Entry(win_g, width=10)
    ent_g51.grid(column=1, row=0, sticky=W)
    ent_g52.grid(column=1, row=1, sticky=W)
    ent_g53.grid(column=1, row=2, sticky=W)
    ent_g54.grid(column=1, row=3, sticky=W)
    ent_g55.grid(column=1, row=4, sticky=W)
    ent_g56.grid(column=1, row=5, sticky=W)
    ent_g51.focus_set()   

    global photo
    photo = tk.PhotoImage(file = './img/trexmer-1.png')
    image_label2 = tk.Label(win_g,image = photo)
    image_label2.place(relx=0.22, rely=0.47)

    but_g51 = Button(win_g, text='Расчитать', command=G51, cursor = 'hand1')
    but_g52 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2')
    but_g51.grid(column=0, row=100)
    but_g52.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def F1():
    win_g = Toplevel()
    win_g.title('Расчёт первой космической скорости')
    win_g.geometry('500x200')
    win_g.resizable(height = False, width = False)    
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Физики. Расчёт первой космической скорости'
    masf.append(s)

    def F():
        if ((ent_f1.get() == '') or (ent_f2.get() == '')):
            lab_f99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_f1.get().isdigit() and ent_f2.get().isdigit()) == False:
            lab_f99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_fiz
            count += 1
            k_fiz += 1
            lab_f99.configure(text=str((6.67408 * (10 ** (-11)) * ((int(ent_f1.get())) / (int(ent_f2.get()))))** 0.5) + ' м/с', fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт первой космической скорости ' + '\n' + 'Масса планеты = '+ ent_f1.get() + ' (кг)' + '\t' + 'Радиус = ' + ent_f2.get() + ' (Км)' + '\t' + '--> ' + str((6.67408 * (10 ** (-11)) * ((int(ent_f1.get())) / (int(ent_f2.get()))))** 0.5) + ' м/с' + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Физики'
            masf.append(s)

    def Del():
        lab_f99.configure(text='')
        ent_f1.delete(0, END)
        ent_f2.delete(0, END)

    def closing():
        radio_var1.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_f1 = Label(win_g, text='Введите массу планеты(кг):')
    lab_f2 = Label(win_g, text='Введите радиус планеты(Км):')
    lab_f98 = Label(win_g, text='Ответ:')
    lab_f99 = Label(win_g, text='')
    lab_f1.grid(column=0, row=0, sticky=W)
    lab_f2.grid(column=0, row=1, sticky=W)
    lab_f98.grid(column=0, row=99, sticky=W)
    lab_f99.grid(column=1, row=99, sticky=W)
    

    ent_f1 = Entry(win_g, width=10)
    ent_f2 = Entry(win_g, width=10)
    ent_f1.grid(column=1, row=0, sticky=W)
    ent_f2.grid(column=1, row=1, sticky=W)
    ent_f1.focus_set()   

    but_f1 = Button(win_g, text='Расчитать', command=F, cursor = 'hand1')
    but_f2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2') 
    but_f1.grid(column=0, row=100)
    but_f2.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def F2():
    win_g = Toplevel()
    win_g.title('Расчёт второй космической скорости')
    win_g.geometry('500x200')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Физики. Расчёт второй космической скорости'
    masf.append(s)

    def F():
        if (ent_f1.get() == '') or (ent_f2.get() == ''):
            lab_f99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_f1.get().isdigit() and ent_f2.get().isdigit()) == False:
            lab_f99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_fiz
            count += 1
            k_fiz += 1
            lab_f99.configure(text=str((2 * 6.67408 * (10 ** (-11)) * ((int(ent_f1.get())) / (int(ent_f2.get()))))** 0.5)  + ' м/с', fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт второй космической скорости ' + '\n' + 'Масса планеты = '+ ent_f1.get() + ' (кг)' + '\t' + 'Радиус = ' + ent_f2.get() + ' (Км)' + '\t' + '--> ' + str((2 * 6.67408 * (10 ** (-11)) * ((int(ent_f1.get())) / (int(ent_f2.get()))))** 0.5) + ' м/с' + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Физики'
            masf.append(s)

    def Del():
        lab_f99.configure(text='')
        ent_f1.delete(0, END)
        ent_f2.delete(0, END)

    def closing():
        radio_var1.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_f1 = Label(win_g, text='Введите массу планеты(кг):')
    lab_f2 = Label(win_g, text='Введите радиус планеты(км):')
    lab_f98 = Label(win_g, text='Ответ:')
    lab_f99 = Label(win_g, text='')
    lab_f1.grid(column=0, row=0, sticky=W)
    lab_f2.grid(column=0, row=1, sticky=W)
    lab_f98.grid(column=0, row=99, sticky=W)
    lab_f99.grid(column=1, row=99, sticky=W)
    

    ent_f1 = Entry(win_g, width=10)
    ent_f2 = Entry(win_g, width=10)
    ent_f1.grid(column=1, row=0, sticky=W)
    ent_f2.grid(column=1, row=1, sticky=W)
    ent_f1.focus_set()   

    but_f1 = Button(win_g, text='Расчитать', command=F, cursor = 'hand1')
    but_f2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2') 
    but_f1.grid(column=0, row=100)
    but_f2.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def F3():
    win_g = Toplevel()
    win_g.title('Расчёт закона всемирного тяготения Ньютона')
    win_g.geometry('500x200')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Физики. Расчёт закона всемирного тяготения Ньютона'
    masf.append(s)

    def F():
        if (ent_f1.get() == '') or (ent_f2.get() == ''):
            lab_f99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)            
        elif (ent_f1.get().isdigit() and ent_f2.get().isdigit()) == False:
            lab_f99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)            
        else:
            global count
            global k_fiz
            count += 1
            k_fiz += 1
            lab_f99.configure(text=str(6.67408 * (10 ** (-11)) * int(ent_f1.get())* int(ent_f2.get()) / (int(ent_f3.get()) ** 2)) + ' ньютон', fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт закона всемирного тяготения Ньютона ' + '\n' + 'Масса 1 = '+ ent_f1.get() + ' (кг)' + '\t' + 'Масса 2 = ' + ent_f2.get() + ' (кг)' + '\t' + 'Радиус = ' + ent_f3.get() + ' (м)' + '\t' + '--> ' + str(6.67408 * (10 ** (-11)) * int(ent_f1.get())* int(ent_f2.get()) / (int(ent_f3.get()) ** 2)) + ' ньютон' + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Физики'
            masf.append(s)

    def Del():
        lab_f99.configure(text='')
        ent_f1.delete(0, END)
        ent_f2.delete(0, END)
        ent_f3.delete(0, END)
        
    def closing():
        radio_var1.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_f1 = Label(win_g, text='Введите массу 1(кг):')
    lab_f2 = Label(win_g, text='Введите массу 2(кг):')
    lab_f3 = Label(win_g, text='Введите радиус между мат. точками(м):')
    lab_f98 = Label(win_g, text='Ответ:')
    lab_f99 = Label(win_g, text='')
    lab_f1.grid(column=0, row=0, sticky=W)
    lab_f2.grid(column=0, row=1, sticky=W)
    lab_f3.grid(column=0, row=2, sticky=W)
    lab_f98.grid(column=0, row=99, sticky=W)
    lab_f99.grid(column=1, row=99, sticky=W)
    

    ent_f1 = Entry(win_g, width=10)
    ent_f2 = Entry(win_g, width=10)
    ent_f3 = Entry(win_g, width=10)
    ent_f1.grid(column=1, row=0, sticky=W)
    ent_f2.grid(column=1, row=1, sticky=W)
    ent_f3.grid(column=1, row=2, sticky=W)
    ent_f1.focus_set()   

    but_f1 = Button(win_g, text='Расчитать', command=F, cursor = 'hand1')
    but_f2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2') 
    but_f1.grid(column=0, row=100)
    but_f2.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def F4():
    win_g = Toplevel()
    win_g.title('Расчёт закона Ома для участка цепи')
    win_g.geometry('500x200')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Физики. Расчёт закона Ома для участка цепи'
    masf.append(s)
    def F():
        if (ent_f1.get() == '') or (ent_f2.get() == ''):
            lab_f99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)           
        elif (ent_f1.get().isdigit() and ent_f2.get().isdigit()) == False:
            lab_f99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)          
        else:
            global count
            global k_fiz
            count += 1
            k_fiz += 1
            lab_f99.configure(text=str(int(ent_f1.get())/ int(ent_f2.get())) + ' ампер', fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт закона Ома для участка цепи ' + '\n' + 'Напряжение = '+ ent_f1.get() + ' (Вольт)' + '\t' + 'Сопротивление = ' + ent_f2.get() + ' (Ом)' + '\t' + '--> ' + str(int(ent_f1.get())/ int(ent_f2.get())) + ' ампер' + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Физики'
            masf.append(s)  

    def Del():
        lab_f99.configure(text='')
        ent_f1.delete(0, END)
        ent_f2.delete(0, END)
        
    def closing():
        radio_var1.set(-1)
        win_g.destroy()        
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_f1 = Label(win_g, text='Введите напряжение(Вольт):')
    lab_f2 = Label(win_g, text='Введите сопротивление(Ом):')
    lab_f98 = Label(win_g, text='Ответ:')
    lab_f99 = Label(win_g, text='')
    lab_f1.grid(column=0, row=0, sticky=W)
    lab_f2.grid(column=0, row=1, sticky=W)
    lab_f98.grid(column=0, row=99, sticky=W)
    lab_f99.grid(column=1, row=99, sticky=W)
    

    ent_f1 = Entry(win_g, width=10)
    ent_f2 = Entry(win_g, width=10)
    ent_f1.grid(column=1, row=0, sticky=W)
    ent_f2.grid(column=1, row=1, sticky=W)
    ent_f1.focus_set()

    but_f1 = Button(win_g, text='Расчитать', command=F, cursor = 'hand1')
    but_f2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2') 
    but_f1.grid(column=0, row=100)
    but_f2.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def F5():
    win_g = Toplevel()
    win_g.title('Расчёт силы')
    win_g.geometry('500x200')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Физики. Расчёт силы'
    masf.append(s)
    def F():
        if (ent_f1.get() == '') or (ent_f2.get() == ''):
            lab_f99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)           
        elif (ent_f1.get().isdigit() and ent_f2.get().isdigit()) == False:
            lab_f99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)
        else:
            global count
            global k_fiz
            count += 1
            k_fiz += 1
            lab_f99.configure(text=str(int(ent_f1.get()) * int(ent_f2.get())) + ' ньютон', fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт силы ' + '\n' + 'Масса = '+ ent_f1.get() + ' (кг)' + '\t' + 'Ускорение = ' + ent_f2.get() + ' (м/с^2)' + '\t' + '--> ' + str(int(ent_f1.get()) * int(ent_f2.get())) + ' ньютон' + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Физики'
            masf.append(s)              

    def Del():
        lab_f99.configure(text='')
        ent_f1.delete(0, END)
        ent_f2.delete(0, END)
        
    def closing():
        radio_var1.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_f1 = Label(win_g, text='Введите массу(кг):')
    lab_f2 = Label(win_g, text='Введите ускорение(м/с^2):')
    lab_f98 = Label(win_g, text='Ответ:')
    lab_f99 = Label(win_g, text='')
    lab_f1.grid(column=0, row=0, sticky=W)
    lab_f2.grid(column=0, row=1, sticky=W)
    lab_f98.grid(column=0, row=99, sticky=W)
    lab_f99.grid(column=1, row=99, sticky=W)
    

    ent_f1 = Entry(win_g, width=10)
    ent_f2 = Entry(win_g, width=10)
    ent_f1.grid(column=1, row=0, sticky=W)
    ent_f2.grid(column=1, row=1, sticky=W)
    ent_f1.focus_set()

    but_f1 = Button(win_g, text='Расчитать', command=F, cursor = 'hand1')
    but_f2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2') 
    but_f1.grid(column=0, row=100)
    but_f2.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)

def F6():
    win_g = Toplevel()
    win_g.title('Расчёт центростремительного ускорения')
    win_g.geometry('500x200')
    win_g.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Физики. Расчёт центростремительного ускорения'
    masf.append(s)
    def F():
        if (ent_f1.get() == '') or (ent_f2.get() == ''):
            lab_f99.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)    
        elif (ent_f1.get().isdigit() and ent_f2.get().isdigit()) == False:
            lab_f99.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)
        else:
            global count
            global k_fiz
            count += 1
            k_fiz += 1
            lab_f99.configure(text=str((int(ent_f1.get()) ** 2) / int(ent_f2.get())), fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт центростремительного ускорения ' + '\n' + 'Скорость = '+ ent_f1.get() + ' (м/сек)' + '  ' + 'Радиус = ' + ent_f2.get() + ' (м)' + ' ' + '--> ' + str((int(ent_f1.get()) ** 2) / int(ent_f2.get())) + ' м/сек^2' + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Физики'
            masf.append(s)

    def Del():
        lab_f99.configure(text='')
        ent_f1.delete(0, END)
        ent_f2.delete(0, END)
        
    def closing():
        radio_var1.set(-1)
        win_g.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s) 

    lab_f1 = Label(win_g, text='Введите скорость(м/сек):', padx = 3)
    lab_f2 = Label(win_g, text='Введите радиус(м):', padx = 3)
    lab_f98 = Label(win_g, text='Ответ:', padx = 3)
    lab_f99 = Label(win_g, text='')
    lab_f1.grid(column=0, row=0, sticky=W)
    lab_f2.grid(column=0, row=1, sticky=W)
    lab_f98.grid(column=0, row=99, sticky=W)
    lab_f99.grid(column=1, row=99, sticky=W)
    

    ent_f1 = Entry(win_g, width=10)
    ent_f2 = Entry(win_g, width=10)
    ent_f1.grid(column=1, row=0, sticky=W)
    ent_f2.grid(column=1, row=1, sticky=W)
    ent_f1.focus_set()
   

    but_f1 = Button(win_g, text='Расчитать', command=F, cursor = 'hand1')
    but_f2 = Button(win_g, text='Очистить', command=Del, cursor = 'hand2') 
    but_f1.grid(column=0, row=100)
    but_f2.grid(column=1, row=100, sticky=W)
    win_g.protocol("WM_DELETE_WINDOW", closing)



def X1():
    win_x = Toplevel()
    win_x.title('Расчёт массы вещества в растворе')
    win_x.geometry('500x200')
    win_x.resizable(height = False, width = False)
    now = datetime.datetime.now()
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Открыт калькулятор Химии. Расчёт массы вещества в растворе'
    masf.append(s)
    
    def X11():
        if (ent_x1.get() == '') or (ent_x2.get() == ''):
            lab_x4.configure(text='Пожалуй, стоит ввести данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные не были введены'
            masf.append(s)
        elif (ent_x1.get().isdigit() and ent_x2.get().isdigit()) == False:
            lab_x4.configure(text='Введите корректные данные', fg = 'red')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Данные введены некорректно'
            masf.append(s)
        else:
            global count
            global k_xim
            count += 1
            k_xim += 1
            lab_x4.configure(text=str(int(ent_x1.get()) * int(ent_x2.get()) / 100) + ' кг', fg = 'black')
            exporting.write(str(count) + ') ' + 'Расчёт массы вещества в растворе ' + '\n' + 'Концентрация = '+ ent_x1.get() + ' (%)' + '\t' + 'Масса = ' + ent_x2.get() + ' (кг)' + '\t' + '--> ' + str(int(ent_x1.get()) * int(ent_x2.get()) / 100) + ' кг' + '\n')
            now = datetime.datetime.now()   
            s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Произведен расчёт в калькуляторе Химии'
            masf.append(s)

    def Del():
        lab_x4.configure(text='')
        ent_x1.delete(0, END)
        ent_x2.delete(0, END)
        
    def closing():
        radio_var1.set(-1)
        win_x.destroy()
        now = datetime.datetime.now()   
        s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрыт калькулятор'
        masf.append(s)
        
    lab_x1 = Label(win_x, text='Введите концентрацию раствора(%):', padx = 3)
    lab_x2 = Label(win_x, text='Введите массу раствора(кг):', padx = 3)
    lab_x3 = Label(win_x, text='Ответ:', padx = 3)
    lab_x4 = Label(win_x, text='                         ')
    lab_x1.grid(column=0, row=0, sticky=W)
    lab_x2.grid(column=0, row=1, sticky=W)
    lab_x3.grid(column=0, row=2, sticky=W)
    lab_x4.grid(column=1, row=2, sticky=W)

    ent_x1 = Entry(win_x, width=10)
    ent_x2 = Entry(win_x, width=10)
    ent_x1.grid(column=1, row=0, sticky=W)
    ent_x2.grid(column=1, row=1, sticky=W)
    ent_x1.focus_set()

    but_x1 = Button(win_x, text='Расчитать', command=X11, cursor = 'hand1')
    but_x2 = Button(win_x, text='Очистить', command=Del, cursor = 'hand2')
    but_x1.grid(column=0, row=100)
    but_x2.grid(column=1, row=100, sticky=W) #Масса вещ-ва
    
    win_x.protocol("WM_DELETE_WINDOW", closing)

lab1 = Label(win, text='Выберите предмет:')
lab2 = Label(win, text='Выберите калькулятор:')
lab3 = Label(win, text='Доп. выбор:', fg='SystemButtonFace')
lab1.grid(column=0, row=0, sticky=W)
lab2.grid(column=0, row=4, sticky=W)
lab3.grid(column=0, row=11, sticky=W)

radio_var = tk.IntVar()
radio_var.set(-1)
radio_var1 = tk.IntVar()
radio_var1.set(-1)
radio_var2 = tk.IntVar()
radio_var2.set(-1)

rad_g = Radiobutton(win, text='Геометрия', value=0, command=GEOM, variable = radio_var, cursor = 'draft_large')
rad_f = Radiobutton(win, text='Физика', value=1, command=FIZ, variable = radio_var, cursor = 'draft_large')
rad_x = Radiobutton(win, text='Химия', value=2, command=XIM, variable = radio_var, cursor = 'draft_large')
rad_g1 = Radiobutton(win, text='Расчёт объема', value=3, command=G1, variable = radio_var1, cursor = 'hand1')
rad_g2 = Radiobutton(win, text='Расчёт площади поверхности', value=4, command=G2, variable = radio_var1, cursor = 'hand1')
rad_g3 = Radiobutton(win, text='Расчёт площади', value=5, command=G3, variable = radio_var1, cursor = 'hand1')
rad_g4 = Radiobutton(win, text='Расчёт периметра', value=6, command=G4, variable = radio_var1, cursor = 'hand1')
rad_g5 = Radiobutton(win, text='Расстояние между двумя точками(по координатам)', value=7, command=G5, variable = radio_var1, cursor = 'hand1')
rad_f1 = Radiobutton(win, text='Расчёт первой космической скорости', value=8, command=F1, variable = radio_var1, cursor = 'hand1')
rad_f2 = Radiobutton(win, text='Расчёт второй космической скорости', value=9, command=F2, variable = radio_var1, cursor = 'hand1')
rad_f3 = Radiobutton(win, text='Расчёт закона всемирного тяготения', value=10, command=F3, variable = radio_var1, cursor = 'hand1')
rad_f4 = Radiobutton(win, text='Расчёт закона Ома', value=11, command=F4, variable = radio_var1, cursor = 'hand1')
rad_f5 = Radiobutton(win, text='Расчёт силы', value=12, command=F5, variable = radio_var1, cursor = 'hand1')
rad_f6 = Radiobutton(win, text='Расчёт центростремительного ускорения при движении по окр', value=13, command=F6, variable = radio_var1, cursor = 'hand1')
rad_x1 = Radiobutton(win, text='Расчёт массы вещества в растворе', value=14, command=X1, variable = radio_var1, cursor = 'hand1')
rad_gd1 = Radiobutton(win, text='Куб', value=15, command=G1cub, variable = radio_var2, cursor = 'right_ptr')
rad_gd2 = Radiobutton(win, text='Пирамида', value=16, command=G1pir, variable = radio_var2, cursor = 'right_ptr')
rad_gd3= Radiobutton(win, text='Конус', value=17, command=G1con, variable = radio_var2, cursor = 'right_ptr')
rad_gd4 = Radiobutton(win, text='Цилиндр', value=18, command=G1shil, variable = radio_var2, cursor = 'right_ptr')
rad_gd5 = Radiobutton(win, text='Шар', value=19, command=G1cr, variable = radio_var2, cursor = 'right_ptr')
rad_gd6 = Radiobutton(win, text='Призма', value=20, command=G1pr, variable = radio_var2, cursor = 'right_ptr')
rad_gd1a = Radiobutton(win, text='Куб', value=31, command=G1cuba, variable = radio_var2, cursor = 'right_ptr')
rad_gd2a = Radiobutton(win, text='Пирамида', value=32, command=G1pira, variable = radio_var2, cursor = 'right_ptr')
rad_gd3a= Radiobutton(win, text='Конус', value=33, command=G1cona, variable = radio_var2, cursor = 'right_ptr')
rad_gd4a = Radiobutton(win, text='Цилиндр', value=34, command=G1shila, variable = radio_var2, cursor = 'right_ptr')
rad_gd5a = Radiobutton(win, text='Шар', value=35, command=G1cra, variable = radio_var2, cursor = 'right_ptr')
rad_gd7 = Radiobutton(win, text='Квадрат', value=21, command=G3cv, variable = radio_var2, cursor = 'right_ptr')
rad_gd7a = Radiobutton(win, text='Квадрат', value=21, command=G3cva, variable = radio_var2, cursor = 'right_ptr')
rad_gd8 = Radiobutton(win, text='Прямоугольник', value=22, command=G3pram, variable = radio_var2, cursor = 'right_ptr')
rad_gd8a = Radiobutton(win, text='Прямоугольник', value=37, command=G3prama, variable = radio_var2, cursor = 'right_ptr')
rad_gd10 = Radiobutton(win, text='Треугольник', value=24, command=G3tr, variable = radio_var2, cursor = 'right_ptr')
rad_gd10a = Radiobutton(win, text='Треугольник', value=38, command=G3tra, variable = radio_var2, cursor = 'right_ptr')
rad_gd11 = Radiobutton(win, text='Трапеция', value=25, command=G3trap, variable = radio_var2, cursor = 'right_ptr')
rad_gd12 = Radiobutton(win, text='Ромб', value=26, command=G3romb, variable = radio_var2, cursor = 'right_ptr')
rad_gd13 = Radiobutton(win, text='Круг', value=27, command=G3crug, variable = radio_var2, cursor = 'right_ptr')
rad_gd13a = Radiobutton(win, text='Круг', value=39, command=G3cruga, variable = radio_var2, cursor = 'right_ptr')
rad_gd14 = Radiobutton(win, text='1-мерная', value=28, command=G51, variable = radio_var2, cursor = 'right_ptr')
rad_gd15 = Radiobutton(win, text='2-мерная', value=29, command=G52, variable = radio_var2, cursor = 'right_ptr')
rad_gd16 = Radiobutton(win, text='3-мерная', value=30, command=G53, variable = radio_var2, cursor = 'right_ptr')
rad_g.grid(column=0, row=1, sticky=W)
rad_f.grid(column=0, row=2, sticky=W)
rad_x.grid(column=0, row=3, sticky=W)

def close_win():
    messagebox.showinfo(title = "Уведомление", message = "Расчёты успешно сохранены в файле output")
    exporting.write('\n' + 'Всего расчётов --- ' + str(count) + '\n')
    exporting.write('Из них физика  --- ' + str(k_fiz) + '\t' +' химия  --- ' + str(k_xim) + '\t' +' математика  --- ' + str(k_math) + '\n\n')    
    exporting.write('----===[Логи]===----' + '\n\n')
    now = datetime.datetime.now()   
    s = str(now.strftime("%d-%m-%Y %H:%M:%S")) + ' | Закрытие программы'
    masf.append(s)
    for x in masf:
        exporting.write(x + '\n')
    win.destroy()
    
win.protocol("WM_DELETE_WINDOW", close_win)
win.mainloop()
exporting.close()
