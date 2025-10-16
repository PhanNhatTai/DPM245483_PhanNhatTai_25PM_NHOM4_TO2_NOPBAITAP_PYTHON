def tinhBMI(chieucao,cannang) :
    return cannang/(chieucao*chieucao)
def phanLoai(BMI) :
    if BMI<18.5 :
        return 'Gầy'
    elif BMI>=18.5 and BMI<=24.9 :
        return 'Bình_Thường'
    elif BMI>=25 and BMI<=29.9 :
        return 'Hơi_Béo'
    elif BMI>=30 and BMI<=34.9 :
        return 'Béo_Phì_Cấp_1'
    elif BMI>=35 and BMI<=39.9 :
        return 'Béo_Phì_Cấp_2'
    elif BMI>40 :
        return 'Béo_Phì_Cấp_3'
def nguyCo(BMI) :
    if BMI<18.5 :
        return 'Thấp'
    elif BMI>=18.5 and BMI<=24.9 :
        return 'Trung_Bình'
    elif BMI>=25 and BMI<=29.9 :
        return 'Cao'
    elif BMI>=30 and BMI<=34.9 :
        return 'Cao'
    elif BMI>=35 and BMI<=39.9 :
        return 'Rất_Cao'
    elif BMI>40 :
        return 'Nguy_Hiểm'
chieucao=float(input("Nhập vào chiều cao (m) :"))
cannang=float(input("Nhập vào cân nặng của bạn (kg) :"))
BMI=tinhBMI(chieucao,cannang)
print("BMI của bạn là :",BMI)
print("\n Phân loại của bạn là :",phanLoai(BMI))
print("\n Nguy cơ của bạn là :",nguyCo(BMI))