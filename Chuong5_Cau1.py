def CheckDoiXung(s,n) :
    check=True
    for i in range (n) :
        if s[i] != s[n-1-i] :
            check=False 
    return check
def main() :
    N=int(input("Nhập vào độ dài của chuỗi :"))
    s=[0] *(N)
    for i in range (N) :
        s[i]=input(f"Nhập vào giá trị của chuỗi ở vị trí {i+1} :")
    check=CheckDoiXung(s,N)
    if check==True :
        print("\nVậy chuỗi bạn nhập đối xứng")
    else :
        print("\nVậy chuỗi bạn nhập không đối xứng")
while True :
    main()
    tiep=input("Bạn muốn nhập tiếp không (c:có,k:không)")
    if (tiep.upper()=='K') :
        break
print("Cảm mơn bạn !!!")
