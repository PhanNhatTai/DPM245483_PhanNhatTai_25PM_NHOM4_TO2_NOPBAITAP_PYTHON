a=float(input("Nhập vào số a:"))
b=float(input("Nhập vào số b:"))
dau=input("Nhập vào phép toán muốn thực hiện (+,-,*,/) :")
while (dau !='+' and dau!='-' and dau !='*' and dau !='/') :
    dau=input("Vui lòng nhập lại phép toán muốn thực hiện (+,-,*,/) :")
if (dau=='+') :
    print(f"Vậy kết quả của phép toán {a} + {b} là :{a+b}")
elif (dau=='-') :
    print(f"Vậy kết quả của phép toán {a} - {b} là :{a-b}")
elif (dau=='*') :
    print(f"Vậy kết quả của phép toán {a} * {b} là :{a*b}")
elif (dau=='/') :
    print(f"Vậy kết quả của phép toán {a} / {b} là :{a/b}")