import string
so=int(input("Nhập vào 1 số (tối đa 2 chữ số):"))
while (so>99) :
    so=int(input("Vui lòng nhập lại số có 2 chữ số :"))
hangchuc=int(so/10)
chuc=''
if (hangchuc==1) : chuc='Muoi'
elif (hangchuc==2) :chuc='Hai muoi'
elif (hangchuc==3) :chuc='Ba muoi'
elif (hangchuc==4) :chuc='Bon muoi'
elif (hangchuc==5) :chuc='Nam muoi'
elif (hangchuc==6) :chuc='Sau muoi'
elif (hangchuc==7) :chuc='Bay muoi'
elif (hangchuc==8) :chuc='Tam muoi'
elif (hangchuc==9) :chuc='Chin muoi'
hangdonvi=so%10
donvi=''
if (hangdonvi==1) : 
    if(so<10) :
        donvi='Một'
    else :
        donvi='mốt'
elif (hangdonvi==2) :donvi='Hai'
elif (hangdonvi==3) :donvi='Ba'
elif (hangdonvi==4) :donvi='Bốn'
elif (hangdonvi==5) :
    if (so<10):
        donvi='Năm'
    else :
        donvi='lăm'
elif (hangdonvi==6) :donvi='Sáu'
elif(hangdonvi==7) :donvi='Bảy'
elif (hangdonvi==8) :donvi='Tám'
elif (hangdonvi==9) :donvi='Chín'
print("số vừa nhập ",so," là :",chuc , donvi)