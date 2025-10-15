import math
tam=1
while tam==1 :
    so=int(input("Nhập vào 1 số :"))
    snt=0
    if (so <0) :
        print(f"Số {so} không phải số nguyên tố :")
    for i in range(2,int(math.sqrt(so))+1) :
        if (so%i==0) :
            print(f"Số {so} không phải số nguyên tố")
            snt+=1
            break
    if (snt==0) :
        print(f"Số {so} là số nguyên tố")
    tam=int(input("Bạn có muốn kiểm tra tiếp không (1 : có , 2 : không):"))
    while tam !=1 and tam !=2 :
        tam=int(input("Vui lòng nhập lại (1 : có , 2 : không) :"))