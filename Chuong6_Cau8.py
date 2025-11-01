n=int(input("Nhập vào số lượng phần tử trong mảng :"))
a=[0]*n
for i in range(0,n) :
    a[i]=float(input(f"Nhập vào giá trị của phần tử thứ {i+1} trong mảng :"))
tam=0
for i in range(0,n-1) :
    for j in range(i,n) :
        if a[i]<a[j] :
            tam=a[i]
            a[i]=a[j]
            a[j]=tam
print("Vậy List sau khi sắp xếp giảm dần là :")
print("\n",a)