from libraries.XL_BMI import *
from tkinter import *

root = Tk()
root.geometry('480x480')
root.resizable(0,0)
root.title("CHUONG TRINH THEO DOI SUC KHOE CUA BAN")
def ketquaBMI():
    chieucao = float(tall.get())
    cannang = float(kilo.get())
    bmi = tinh_bmi(chieucao,cannang)
    kqBMI.set(round(bmi,2))
    ketluan.set(ket_luan(bmi))
def reset():
    tall.set('')
    kilo.set('')
    kqBMI.set('')
    ketluan.set('')
#hinh
photo = PhotoImage(file="bmi.png")
Label(root,image=photo).grid(row=0,column=0)
#chieucao
Label(root,text="Chieu cao cua ban (met):").grid(row=1,column=1)
tall = StringVar()

entrytall = Entry(root,width=30,textvariable=tall).grid(row=1,column=2)
#can nang
Label(root,text="Can nang cua ban (kg):").grid(row=2,column=1)
kilo = StringVar()

entrykilo = Entry(root,width=30,textvariable=kilo).grid(row=2,column=2)
#Ket qua
kqBMI = StringVar()
ketluan = StringVar()
#bmi
Label(root,text="Chi so BMI:").grid(row=4,column=1)
entryBMI = Entry(root,textvariable=kqBMI,width=40).grid(row=4,column=2)
#ket luan
Label(root,text="Danh gia suc khoe:").grid(row=5,column=1)
entryketluan = Entry(root,textvariable=ketluan,width=40).grid(row=5,column=2)
#reset
Button(root,text="RESET",width=5,command=reset).grid(row=6,column=1)
#Thoat
Button(root,text="Quit",width=5,command=root.quit).grid(row=6,column=2)

#tinh BMI
Button(root,text="Tinh BMI",width=10,command=ketquaBMI).grid(row=3,column=2)

root.mainloop()
