"""
from tkinter import *
def Ok() :
    a=Taikhoang.get()
    b=Mk.get()
    tb=Tb.get()
Taikhoang=StringVar()
Mk=StringVar()
Tb=StringVar()
root=Tk()
root.title("Hello")
root.minsize(height=150,width=250)
root.resizable(height=True,width=True)
Label(root,text="Đăng Nhập",justify=CENTER).grid(row=0,columnspan=3)
Label(root,text="Tài Khoản :").grid(row=1,column=0)
Entry(root,width=40,textvariable=Taikhoang).grid(row=1,column=1)
Label(root,text="Mật Khẩu :").grid(row=2,column=0)
Entry(root,width=40,textvariable=Mk).grid(row=2,column=1)
Nut=Frame()
Button(Nut,text="OK",command=Ok).pack(side=LEFT)
Button(Nut,text="Cancel",command=root.quit).pack(side=LEFT)
Nut.grid(row=3,columnspan=2)
root.mainloop()
"""