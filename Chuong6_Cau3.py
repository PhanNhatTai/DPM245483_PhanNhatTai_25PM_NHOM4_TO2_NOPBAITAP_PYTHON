from random import randrange
def main() :
    m=int(input("Nhập vào số dòng :"))
    n=int(input("Nhập vào số cột :"))
    A=TaoMaTran(m,n)
    XuatMaTran(A)
    k=int(input("Nhập vào dòng bạn muốn xuất ra màn hình :"))
    C=XuatDong(k-1,A)
    print(f"\nVậy dòng {k} trong ma trận có các giá trị là :{C}")
    l=int(input("Nhập vào cột bạn muốn xuất ra màn hình :"))
    D=XuatCot(l,A)
    print(f"\nVậy cột {l} trong ma trận có các giá trị là :{D}")
    lon=SoMaxTrongMaTran(A)
    print(f"\nVậy số lớn nhất trong ma trận là :{lon}")
def TaoMaTran(m,n) :
    A=[]
    for i in range(m) :
        row=[]
        for j in range(n) :
            row.append(randrange(0,100))
        A.append(row)
    return A
def XuatMaTran(A) :
    for i in A:
        print(i)    
def XuatDong(k,A) :
    C=[]
    for i in A :
        for j in range(0,len(i)) :
            if j==k :
                C.append(i[j])
    return C
def XuatCot(l,A) :
    D=[]
    dong=1
    for i in A :
        if dong==l :
            D.append(i)
        dong+=1
    return D
def SoMaxTrongMaTran(A) :
    lon=0
    for i in A:
        for j in range(0,len(i)) :
            if lon<i[j] :
                lon=i[j]
    return lon
main()
