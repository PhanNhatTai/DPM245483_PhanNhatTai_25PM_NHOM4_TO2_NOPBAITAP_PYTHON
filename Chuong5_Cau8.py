def TachLayMp3 (s) :
    chuoi=[]
    chuoi_moi=s.split("//")
    for tu in chuoi_moi :
        if tu.endswith(".mp3") :
            chuoi=tu
    return chuoi
def LayTenBaiHat (s) :
    chuoi=""
    chuoi_moi=s.split("//")
    i=0
    check=0
    for tu in chuoi_moi :
        if tu.endswith(".mp3") :
            while i<len(tu) and check ==0:
                if tu[i]!='.' :
                    chuoi=chuoi+tu[i]
                elif tu[i]=='.' :
                    check+=1
                i+=1
    return chuoi
def main() :
    s=input("Nhap vao 1 duong dan ban muon :")
    s=TachLayMp3(s)
    print(s)
    s=LayTenBaiHat(s)
    print(s)
main()