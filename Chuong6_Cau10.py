def TaoMaTran(m,n) :
    a=[]
    for i in range(0,m) :
        dong=[0]*n
        for j in range(0,n) :
            dong[j]=float(input(f"Nhập vào giá trị của phần tử dòng {i+1} cột {j+1} trong list :"))
        a.append(dong)
    return a
def InMaTran(a) :
    for i in a :
        print(i)
def Cong2MaTran(a,b,m,n) :
    d=[]
    for j in range(m) :
        dong=[]
        for i in range (n) :
            giatri=a[j][i]+ b[j][i]
            dong.append(giatri)
        d.append(dong)
    return d
m1=int(input("Nhập vào số dòng của ma trận a:"))
n1=int(input("Nhập vào số cột của ma trận a:"))
A=TaoMaTran(m1,n1)
m2=int(input("Nhập vào số dòng của ma trận b:"))
n2=int(input("Nhập vào số cột của ma trận b:"))
B=TaoMaTran(m2,n2)
print("Ma trận A:")
InMaTran(A)
print("\nMa trận B:")
InMaTran(B)
while m1!=m2 or n1!=n2:
    print("Ma trận của bạn nhập không thể cộng được vui lòng nhập lại 2 ma trận khác để cộng :")
    m1=int(input("Nhập vào số dòng của ma trận a:"))
    n1=int(input("Nhập vào số cột của ma trận a:"))
    A=TaoMaTran(m1,n1)
    m2=int(input("Nhập vào số dòng của ma trận b:"))
    n2=int(input("Nhập vào số cột của ma trận b:"))
    B=TaoMaTran(m2,n2)
    print("Ma trận A:")
    InMaTran(A)
    print("\nMa trận B:")
    InMaTran(B)
Cong2matran=Cong2MaTran(A,B,m1,n1)
print("\nVậy kết quả của 2 ma trận sau khi cộng là :")
InMaTran(Cong2matran)
#Còn hàm tìm ma trận hoán vị
