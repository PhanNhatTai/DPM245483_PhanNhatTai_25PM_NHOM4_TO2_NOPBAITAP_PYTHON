import math
def TinhDoDai2Diem(Xa,Xb,Ya,Yb) :
    return math.sqrt((Xb-Xa)**2 + (Yb-Ya)**2)
Xa=float(input("Nhập vào hoành dộ x :"))
Ya=float(input("Nhập vào tung dộ x :"))
Xb=float(input("Nhập vào hoành độ y :"))
Yb=float(input("Nhập vào tung độ b :"))
Dodai=TinhDoDai2Diem(Xa,Xb,Ya,Yb)
print(f"Vậy độ dài 2 cạnh A và B là :{Dodai}")