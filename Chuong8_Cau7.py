from tkinter import *
def Chuyen() :
    Nam=int(nam.get())
    can=("Canh","Tân","Nhâm","Quý","Giáp","Ất","Bính","Đinh","Mậu","Kỷ")
    giap=("Thân","Dậu","Tuất","Hợi","Tí","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi")
    Can=Nam%10
    Chi=Nam%12
    ten_can=can[Can]
    ten_chi=giap[Chi]
    canchi.set(f"{ten_can} {ten_chi}")
root=Tk()
root.title("Chuyển lịch")
root.minsize(height=150,width=250)
root.resizable(height=True,width=True)
nam=StringVar()
canchi=StringVar()
Label(root,text="Nhập năm dương").grid(row=0,column=0)
Entry(root,width=50,textvariable=nam).grid(row=0,column=1)
Nut=Frame()
Button(Nut,text="Chuyển",justify=CENTER,command=Chuyen).pack(side=LEFT)
Nut.grid(row=1,columnspan=2)
Label(root,text="Năm âm").grid(row=2,column=0)
Entry(root,width=50,textvariable=canchi).grid(row=2,column=1)
root.mainloop()