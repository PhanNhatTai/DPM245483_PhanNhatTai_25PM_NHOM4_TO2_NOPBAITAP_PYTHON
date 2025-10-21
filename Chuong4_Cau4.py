def ROI (Doanhthu,Chiphi) :
    return (Doanhthu-Chiphi)/Chiphi
def Kq (ROI) :
    if ROI >=0.75 :
        print("Bạn nên đầu tư")
    else :
        print("Bạn không nên đầu tư")
print("Chương trình tính ROI")
Doanhthu=int(input("Nhập vào doanh thu :"))
Chiphi=int(input("Nhập vào chi phí :"))
roi=float(ROI(Doanhthu,Chiphi))
print(f"Vậy ROI của bạn là :{roi}")
Kq(roi)