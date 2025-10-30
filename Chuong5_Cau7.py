def ToiUuChuoi(s) :
    danh_sach_tu=s.split()
    danh_sach_chuan_hoa=[so.capitalize() for so in danh_sach_tu]
    return " ".join(danh_sach_chuan_hoa)
def main() :
    s=input("Nhập vào 1 chuỗi :")
    s=ToiUuChuoi(s)
    print(s)
main()
