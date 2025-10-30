import math
def SoNguyenTo (s) :
    check=1
    if s==1 or s==2 :
        check=0
    for i in range (2,int(math.sqrt(s)+1)) :
        if s%i==0 :
            check=0
    return check
s=input("Nhập vào 1 chuỗi :")
print(s)
so=s.split(";")
print(so)
chan=0
le=0
snt=0
for i in so :
    number=int(i)
    if number%2==0 :
        chan+=1
    elif number%2==1 :
        le+=1
    check=SoNguyenTo(number)
    if check==1:
        snt+=1
print("Vậy số lượng số chẳn trong mảng là :",chan)
print("Vậy số lượng số lẻ trong mảng là :",le)
print("Vậy số lượng số nguyên tố trong mảng là :",snt)
