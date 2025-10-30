def ToiUuChuoi(s) :
    s2=s
    s2=s2.strip()
    arr=s2.split()
    s2=''
    for i in arr :
        word =i
        if len(word.strip())!=0: 
            s2=s2+word+" " 
    return s2.strip()
s="    Phan      Nhật     Tài    "
print(s,"có độ dài :",len(s))
s=ToiUuChuoi(s)
print(s,"có độ dài là :",len(s))