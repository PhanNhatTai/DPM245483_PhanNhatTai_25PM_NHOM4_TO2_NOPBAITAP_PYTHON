import random
solan=0
songaunhien=random.randrange(1,101)
while solan<7 :
    solan+=1
    sochon=int(input("Nhập vào số bạn chọn (từ 1-100) :"))
    while (sochon<1 or sochon>100) :
        sochon=int(input("Vui lòng chọn lại (từ 1-100) :"))
    if (sochon<songaunhien) :
        print("Số bạn chọn bé hơn số đúng :")
        print(f"Số lần đã đoán là {solan}")
    elif (sochon>songaunhien) :
        print("Số bạn chọn lớn hơn số đúng :")
        print(f"Số lần đã đoán là {solan}")
    elif(sochon==songaunhien) :
        print(f"Bạn đã đoán đúng số ngẫu nhiên là :{songaunhien}")
        print(f"Số lần đã đoán là {solan}")
        break
if solan ==7 :
    print("Bạn đã đoán quá số lần quy định")