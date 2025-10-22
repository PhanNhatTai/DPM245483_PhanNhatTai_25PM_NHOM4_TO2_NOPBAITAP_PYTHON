import math
def Tinhcanbac2longnhau (n) :
    kq=0
    for i in range (1,n+1) :
        kq=math.sqrt(2+kq)
    return kq
n=int(input("Nhập vào số dấu căn muốn lồng nhau :"))
kq=Tinhcanbac2longnhau(n)
print(f"Vậy kết quả của phép tính căn 2 được lặp lại {n} lần là :{kq} ")