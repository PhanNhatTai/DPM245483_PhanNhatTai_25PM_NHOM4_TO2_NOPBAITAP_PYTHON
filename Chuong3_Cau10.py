x=float(input("Nhập vào x :"))
n=int(input("Nhập vào n :"))
kq=0
for i in range (1,n+1) :
    tu=x**i
    mau=1
    for j in range (1,i+1) :
        mau*=j
    kq+=tu/mau
print("Kết quả :",kq)
    