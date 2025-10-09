ngay=int(input("Nhập vào ngày :"))
while(ngay<1 or ngay >31) :
    ngay=int(input("Vui lòng nhập lại ngày phù hợp :"))
thang=int(input("Nhập vào tháng :"))
while(thang<1 or thang >12) :
    thang=int(input("Vui lòng nhập lại tháng :"))
nam=int(input("Nhập vào năm :"))
ngayke=ngay+1
thangke=thang
namke=nam
if(thang==2) :
    if((nam%4==0 and nam%100!=0) or nam%400==0) :
        if(ngayke>29):
            ngayke=1
            thangke=thang+1
    else :
        if(ngayke>28) :
            ngayke=1
            thangke=thang+1
if(thang==4 or thang==6 or thang==9 or thang==1) :
    if(ngayke>30):
        ngayke=1
        thangke=thang+1
else :
    if(ngayke>31):
        ngayke=1
        thangke=thang+1
if (thangke>12) :
    ngayke=1
    thangke=1
    namke=nam+1
print("Vậy ngày kế tiếp của ngày",ngay,"/",thang,"/",nam,"là :",ngayke,"/",thangke,"/",namke)