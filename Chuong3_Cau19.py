x=int(input("Nhập vào x :"))
n=int(input("Nhập vào n :"))
kq=0
for i in range (0,n+1) :
    tu=x**(2*i+1)
    mau=1
    mautam=2*i+1
    for j in range (1,mautam+1) :
        mau*=j
    kq+=(tu/mau)
print("Vậy kết quả là :",kq)