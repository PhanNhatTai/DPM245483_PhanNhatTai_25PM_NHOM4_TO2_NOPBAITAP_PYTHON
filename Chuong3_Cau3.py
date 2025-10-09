#ax^2+bx+c
from math import sqrt
a=int(input("Nhập vào số a :"))
b=int(input("Nhập vào số b :"))
c=int(input("Nhập vào số c :"))
if (a==0) :
    if(b==0 and c==0) :
        print ("Vậy phương trình có vô số nghiệm")
    elif (b==0 and c!=0) :
        print("Vậy phương trình vô nghiệm") 
    elif (b!=0 and c!=0) :
        print("Vậy phương trình có 1 nghiệm :",-c/b)
else :
    delta=b*b-4*a*c
    if(delta <0) :
        print("Vậy phương trình vô nghiệm")
    elif(delta==0) :
        print("Vậy phương trình có nghiệm kép :",-b/(2*a))
    else :
        print("Vậy phương trình có 2 nghiệm phân biệt :\n")
        print("x1=",(-b-sqrt(delta))/(2*a),"/n")
        print("x2=",(-b+sqrt(delta))/(2*a),"/n")