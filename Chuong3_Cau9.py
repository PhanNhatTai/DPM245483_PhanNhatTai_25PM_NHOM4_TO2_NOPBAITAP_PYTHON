thang=int(input("Nhập vào 1 tháng :"))
while thang <1 or thang >12 :
    thang=int(input("Vui lòng nhập lại 1 tháng :"))
if thang in range (1,4) :
    print("Tháng thuộc quý 1 !")
elif thang in range (4,7) :
    print("Tháng thuộc quý 2 !")
elif thang in range (7,10) :
    print ("Tháng thuộc quý 3 !")
else :
    print("Tháng thuộc quý 4 !")