from tkinter import *
import math
def Tiep() :
    A.set("")
    B.set("")
    C.set("")
    Kq.set("")
def Giai() :
    a=float(A.get()) 
    b = float(B.get()) 
    c = float(C.get()) 
    if a==0:#bx+c=0 
        if b==0 and c==0: 
            Kq.set("Vô số nghiệm") 
        elif b==0 and c!=0: 
            Kq.set("Vô nghiệm") 
        else: 
            x=-c/b 
            Kq.set("x="+str(x)) 
    else: 
        delta=b**2-4*a*c 
        if delta<0: 
            Kq.set("Vô nghiệm") 
        elif delta==0: 
            Kq.set("No kép x1=x2="+str((-b/(2*a)))) 
        else: 
            x1=(-b- math.sqrt(delta))/(2*a) 
            x2 = (-b + math.sqrt(delta)) / (2 * a) 
            Kq.set("x1="+str(x1)+";x2="+str(x2))
root=Tk()
A=StringVar()
B=StringVar()
C=StringVar()
Kq=StringVar()
root.title("Giải phương trình bậc 2")
root.minsize(height=150,width=250)
root.resizable(height=True,width=True)
Label(root,text="Phương Trình Bậc 2",justify=CENTER).grid(row=0,columnspan=2)
Label(root,text="a").grid(row=1,column=0)
Entry(root,width=50,textvariable=A).grid(row=1,column=1)
Label(root,text="b").grid(row=2,column=0)
Entry(root,width=50,textvariable=B).grid(row=2,column=1)
Label(root,text="c").grid(row=3,column=0)
Entry(root,width=50,textvariable=C).grid(row=3,column=1)
frameNut=Frame()
Button(frameNut,text="Giải",comman=Giai).pack(side=LEFT)
Button(frameNut,text="Tiếp",command=Tiep).pack(side=LEFT)
Button(frameNut,text="Thoát",command=root.quit).pack(side=LEFT)
frameNut.grid(row=4,columnspan=2)
Label(root,text="Kq").grid(row=5,column=0)
Entry(root,width=50,textvariable=Kq).grid(row=5,column=1)
root.mainloop()
