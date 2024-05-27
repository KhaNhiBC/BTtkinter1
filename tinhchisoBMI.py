from libraries.XL_BMI import *
from tkinter import *
root = Tk()
root.resizable(height=False,width=False)
root.minsize(height=480,width=480)
root.title("CHUONG TRINH THEO DOI SUC KHOE CUA BAN")
photo = PhotoImage(file="bs.jpg")
Label(root,image=photo,relief=RAISED).pack(side=TOP,pady=5)
Label(root,text="Chieu cao cua ban:").pack(side=BOTTOM,pady=5,padx=5)


root.mainloop()
