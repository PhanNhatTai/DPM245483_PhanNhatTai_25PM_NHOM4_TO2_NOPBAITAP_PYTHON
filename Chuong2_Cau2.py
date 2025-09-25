"""
Nhập vào số giây bất kỳ  t. Tính và xuất ra dạng  
Giờ:Phút:Giây 
"""
t=int(input("Nhập số giây:")) 
hour=(t//3600)%24 
minute=(t%3600)//60 
second=(t%3600)%60 
print(hour,":",minute,":",second)
