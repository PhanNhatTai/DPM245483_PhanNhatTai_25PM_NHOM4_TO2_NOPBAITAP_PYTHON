import math
a=float(input("Nhập vào cạnh a :"))
b=float(input("Nhập vào cạnh b :"))
c=float(input("Nhập vào cạnh c :"))
while ((a<=0 or b<=0 or c<=0) or ((a+b<=c) or (a+c<=b) or (b+c<=a))) :
    print("Tam giác không hợp lệ vui lòng nhập lại :\n")
    a=float(input("Nhập vào cạnh a :"))
    b=float(input("Nhập vào cạnh b :"))
    c=float(input("Nhập vào cạnh c :"))
cv=float(a+b+c)
p=float(cv/2)
dt=float(math.sqrt(p*(p-a)*(p-b)*(p-c)))
print(f"Vậy diện tích của tam giác có 3 cạnh {a} {b} {c} là :{dt}")
