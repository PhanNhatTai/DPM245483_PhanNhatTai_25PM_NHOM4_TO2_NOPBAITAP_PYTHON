from tkinter import *
def BamNut(t) :
    global bieuthuc
    bieuthuc=bieuthuc+str(t)
    hienthi.set(bieuthuc)
def Bang():
    global bieuthuc
    try :
        kq=str(eval(bieuthuc))
        hienthi.set(kq)
        bieuthuc=kq
    except Exception as e:
        hienthi.set("Biểu thức không hợp lệ")
        bieuthuc=""
def Xoa() :
    global bieuthuc
    bieuthuc=""
    hienthi.set("")
root=Tk()
hienthi=StringVar()
bieuthuc=""
root.title("Máy tính")
root.minsize(height=150,width=250)
root.resizable(height=FALSE,width=FALSE)
Entry(root,textvariable=hienthi,justify='right').grid(row=0, columnspan=4, padx=5, pady=5)
buttons = [
    ("1",1,0), ("2",1,1), ("3",1,2),
    ("4",2,0),("5",2,1),("6",2,2),
    ("7",3,0),("8",3,1),("9",3,2),
    ("-",4,0),("0",4,1),(".",4,2),
    ("+",5,0),("-",5,1),("*",5,2),("/",5,3)
]
for (text,row,col) in buttons :
    Button(root,text=text,padx=20, pady=20,command=lambda t=text:BamNut(t)).grid(row=row,column=col ,sticky="nsew")
Button(root,text="=",padx=20,pady=20,command=Bang).grid(row=5,column=4)
Button(root,text="Clr",padx=20,pady=20,command=Xoa).grid(row=6,columnspan=4)
root.mainloop()