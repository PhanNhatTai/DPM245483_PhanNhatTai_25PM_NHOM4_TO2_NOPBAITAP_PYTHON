import string
s=input("Nhập vào 1 chuỗi :")
hoa=0
thuong=0
so=0
kytudatbiet=0
khoangtrang=0
nguyenam=0
phuam=0
NguyenAm="aăâeêioôơuưy"
PhuAm="bcdđghklmnpqrstvx"

for i in s :
    if i.isupper() :
        hoa+=1
    elif i.islower() :
        thuong+=1
    elif i.isdigit() :
        so+=1
    elif i in string.punctuation :
        kytudatbiet+=1
    elif i==' ':
        khoangtrang+=1
    elif i.lower in NguyenAm :
        nguyenam+=1
    elif i.lower in PhuAm :
        phuam+=1
print("Số lương chữ hoa là :",hoa)
print("Số lượng chữ thường là :",thuong)
print("Số lượng số là :",so)
print("Số ký tự đặt biệt là :",kytudatbiet)
print("Số lượng khoảng trắng là :",khoangtrang)
print("Số lượng nguyên âm là :",nguyenam)
print("Số lượng phụ âm là :",phuam)