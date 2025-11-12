from tkinter import *
def Tiep() :
    A.set("")
    B.set("")
    Kq.set("")
def Giai() :
    a=float(A.get())
    b=float(B.get())
    if a==0 and b==0 :
        Kq.set("Phương trình vô số nghiệm")
    elif a==0 and b!=0 :
        Kq.set("Phương trình vô nghiệm") 
    else :
        Kq.set("x="+str((-b/a)))
root=Tk()
A=StringVar()
B=StringVar()
Kq=StringVar()
root.title("Giải phương trình bậc 1 !")
root.minsize(height=150,width=250)
root.resizable(height=True,width=True)
Label(root,text=("Phương Trình Bậc I"),fg="blue",justify=CENTER).grid(row=0,columnspan=2)
Label(root,text=("a")).grid(row=1,column=0)
Entry(root,width=50,textvariable=A).grid(row=1,column=1)
Label(root,text="b").grid(row=2,column=0)
Entry(root,width=50,textvariable=B).grid(row=2,column=1)
frameNut=Frame()
Button(frameNut,text="Giải",command=Giai).pack(side=LEFT)
Button(frameNut,text="Tiếp",command=Tiep).pack(side=LEFT)
Button(frameNut,text="Thoát",command=root.quit).pack(side=LEFT)
frameNut.grid(row=3,columnspan=2)
Label(root,text="Kết quả:").grid(row=4,column=0) 
Entry(root,width=50,textvariable=Kq).grid(row=4,column=1) 
root.mainloop()
