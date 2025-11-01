import math
def SoChan(a) :
    b=[]
    for i in a:
        if i%2==0:
            b.append(i)
    return b
def SoLe(a) :
    c=[]
    for i in a:
        if i%2!=0:
            c.append(i)
    return c
def SoNguyenTo(so) :
    for i in range (2,int(math.sqrt(so)+1)) :
        if so%i==0 :
            return 0
    return 1
n=int(input("Nhập vào số lượng phần tử trong list :"))
a=[0]*n
for i in range(0,n) :
    a[i]=int(input(f"Nhập vào giá trị ở vị trí thứ {i+1} trong list :"))
b=SoChan(a)
Chan=len(b)
print("\nVậy các số chẵn trong list gồm :")
print(b)
print(f"Vậy trong list có {Chan} số chẵn")
c=SoLe(a)
Le=len(c)
print("\nVậy các số lẻ trong list gồm :")
print(c)
print(f"Vậy trong list có {Le} số lẻ")
print("\nCác số nguyên tố trong list là :")
for i in range(0,n) :
    check=SoNguyenTo(a[i]) 
    if check==1 :
        print(a[i],end=' ')
print("\nCác số không phải số nguyên tố trong list là :")
for i in range(0,n) :
    check=SoNguyenTo(a[i]) 
    if check==0 :
        print(a[i],end=' ')