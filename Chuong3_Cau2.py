thang=int(input("Nhập vào 1 tháng :"))
while (thang<1 or thang >12) :
    thang=int(input("Vui lòng nhập lại tháng :"))
if (thang == 4 or thang ==6 or thang==9 or thang==11) :
    print("Vậy tháng ",thang," có 30 ngày")
elif (thang==2) :
    nam=int(input("Vui lòng nhập vào năm :"))
    if ((nam%4==0 and nam%100!=0) or nam%400==0) :
        print("Vậy tháng 2 của năm",nam," có 29 ngày")
    else :
        print("Vậy tháng 2 của năm",nam,"có 28 ngày")
else :
    print("Vậy tháng",thang," có 31 ngày")