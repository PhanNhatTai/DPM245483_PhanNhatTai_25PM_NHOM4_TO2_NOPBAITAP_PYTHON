from random import randrange
def KtDoiXung(a,n) :
    dau=0
    cuoi=n-2
    while dau<n or cuoi>0 :
        if a[dau] != a[cuoi] :
            return 0
        dau+=1
        cuoi-=1
    return 1 
a=[]
n=int(input("Nhập vào số lượng phần tử trong list :"))
for i in range(0,n) :
    a.append(randrange(0,100))
print(a)
k=int(input("Nhập số bạn muốn xoá ra khỏi chuỗi :"))
while a.count(k)>0 :
    a.remove(k)
print(f"\nList sau khi xoá số {k} ra khỏi list là :{a}")
check=KtDoiXung(a,n)
if check==1 :
    print("\nVậy list đối xứng")
elif check==0 :
    print("\nVậy list không đối xứng")