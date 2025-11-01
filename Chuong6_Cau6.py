import random
#Cách tạo list ngầu nhiên không trùng nhau 
n=int(input("Nhập vào số lượng số trong list :"))
Gioihan=range(0,100)
a=random.sample(Gioihan,n)
print("Vậy các phần tử trong list không trùng nhau là :")
print(a)