"""
Viết chương trình nhập vào điểm ba môn Toán, Lý, Hóa của một học sinh. In ra 
điểm trung bình của học sinh đó với hai số lẻ thập phân.
"""
DiemToan=float(input("Nhập vào điểm toán :"))
DiemLy=float(input("Nhập vào điểm lý :"))
DiemHoa=float(input("Nhập vào điểm hóa :"))
DiemTB=(DiemToan+DiemLy+DiemHoa)/3
print("Vậy điểm trung bình là :",round(DiemTB,2))