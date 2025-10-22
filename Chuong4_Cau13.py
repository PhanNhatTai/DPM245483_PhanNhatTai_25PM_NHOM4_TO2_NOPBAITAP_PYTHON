import math
def Tonguoc(so) :
    kq=0
    for i in range (1,so) :
        if so%i==0 :
            kq+=i
    return kq
so=int(input("Nhập vào số nguyên dương cần kiểm tra :"))
while so<0 :
    so=int(input("Vui lòng nhập lại số nguyên dương :"))
kq=Tonguoc(so)
if so==kq :
    print(f"Vậy số {so} là số hoàn thiện")
elif so<kq :
    print(f"Vậy số {so} là số thịnh vượng")   
else :
    print(f"Vậy {so} không phải là số hoàn thiện và số thịnh vượng") 