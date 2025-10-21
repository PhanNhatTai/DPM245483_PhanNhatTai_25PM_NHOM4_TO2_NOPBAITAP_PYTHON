def TraVeGiaTriViTriBatKi(so) :
    return f[so-1] + f[so-2]
def Fib(N) :
    for i in range (3,N+1) :
        f[i]=f[i-1]+f[i-2]
        print(f"f[{i}] = {f[i]}")
N=int(input("Nhập vào giá trị N :"))
f = [0] * (N+1)
if (N>=1) :
    f[1]=1
    print(f"f[1] = {f[1]}")
if (N>=2) :
    f[2]=1
    print(f"f[2] = {f[2]}")
Fib(N)
so=int(input("Nhập vào vị trí bạn tìm (nhỏ hơn N) :"))
while so<=0 or so>N :
    so=int(input("Vui lòng nhập lại vị trí bạn cần tìm :"))
GiaTriCanTim = TraVeGiaTriViTriBatKi(so)
print(f"Vậy vị trí bạn cần tìm là f[{so}] = {GiaTriCanTim}")

