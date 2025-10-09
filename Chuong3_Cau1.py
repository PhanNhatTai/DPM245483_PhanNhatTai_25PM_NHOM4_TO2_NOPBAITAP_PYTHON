nam=int(input("Nhập vào 1 năm :"))
if ((nam%4==0 and nam%100!=0) or nam%400==0) :
    print("Vậy năm",nam," là năm nhuận")
else :
    print("Vậy năm ",nam," là năm không nhuận")
