def  NegativeNumberInStrings(str) :
    chuoi_moi=[]
    i=0
    while i<len(str) :
        if str[i] == '-' :
            if i+1<len(str) and str[i+1].isdigit() :
                chuoi_am='-'
                j=i+1
                while j<len(str) and str[j].isdigit() :
                    chuoi_am=chuoi_am+str[j]
                    j+=1
                i=j
                chuoi_moi.append(chuoi_am)
            else :
                i+=1
        else :
            i+=1
    return chuoi_moi
def main () :
    s=input("Nhập vào 1 chuỗi :")
    chuoi_moi=NegativeNumberInStrings(s)
    print(chuoi_moi)
main()
    
