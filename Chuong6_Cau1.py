import math
def KTSoNguyenTo(so) :
    if so==1 or so==2 : 
        return 0
    for i in range(2,int(math.sqrt(so)+1)):
        if so%i==0 :
            return 0
    return 1
n=int(input("Nhập vào số lượng phần tử trong list :"))
a=[0]*n
for i in range(0,n) :
    a[i]=int(input(f"Nhập vào giá trị thứ {i+1} trong mảng :"))
while True :
    print("\nMời bạn nhập thêm phần tử vào list :")
    Value=int(input())
    a.append(Value)
    chon=input("\nBạn muốn thêm tiếp không (Bấm k để ngưng thêm tiếp số vào list):")
    if chon.lower()=='k' :
        break
k=int(input("Nhập vào giá trị bạn muốn kiểm tra số lần xuất hiện trong list :"))
dem=0
for i in range(0,len(a)):
    if k==a[i] :
        dem+=1
# hoặc có thể dùng dem=a.count(k) để đếm
print(f"Vậy số {k} xuất hiện {dem} lần trong mảng")
TongSNT=0
for i in range(0,int(len(a))) :
    KtSNT=KTSoNguyenTo(a[i])
    if KtSNT==1 :
        TongSNT+=a[i]
print(f"\nTổng các số nguyên tố trong mảng là :{TongSNT}")
a.sort()
"""
tam=0
for i in range(0,len(a)) :
    for j in range(i+1,len(a)) :
        if a[i] >a[j] :
            tam=a[i]
            a[i]=a[j]
            a[j]=tam
"""
# hoặc có thể dùng a.sort() để sắp xếp
print("\nList sau khi sắp xếp tăng dần là :")
print(a)
del a


