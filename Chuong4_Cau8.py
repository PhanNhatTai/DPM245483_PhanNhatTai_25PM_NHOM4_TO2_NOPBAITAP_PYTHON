import math
def Tinhlogax (a,x) :
    return math.log10(x)/math.log10(a)
a=float(input("Nhập vào số a :"))
x=float(input("Nhập vào số x :"))
logax=Tinhlogax(a,x)
print(f"Vậy log{a}[{x}] = {logax}")