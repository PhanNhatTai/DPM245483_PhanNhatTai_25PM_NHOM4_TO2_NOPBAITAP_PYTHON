n=int(input("Nhập vào số lượng phần tử trong list :"))
a=[0]*n
while True :
    dem=0
    for i in range (0,n) :
        a[i]=int(input(f"Nhập vào giá trị của phần tử thứ {i+1} trong list :"))
    for i in range (0,n-1) :
        if a[i] < a[i+1] :
            dem+=1
    if dem==(n-1) :
        break
    else :
        print("Bạn đã nhập sai quy cách vui lòng nhập lại đúng quy cách :")
print(f"List bạn đã nhập là :{a}")