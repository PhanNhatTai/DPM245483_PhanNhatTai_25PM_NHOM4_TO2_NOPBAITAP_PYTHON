for i in range (1,5) :
    for j in range(1,5) :
        if i==2 and j==2 or i==2 and j==3 or i==3 and j==2 or i==3 and j==3 :
            print("",end='\t')
        else :
            print("*",end='\t')
    print("\n")
print("\n")
for i in range (1,5) :
    for j in range(1,5) :
        if i==1 and j==1 or i==1 and j==2 or i==1 and j==3 or i==2 and j==1 or i==2 and j==2 or i==3 and j==1:
            print("",end='\t')
        else :
            print("*",end='\t')
    print("\n")
print("\n")
for i in range (1,8) :
    for j in range(1,8) :
        if  i==1 and j==1 or i==2 and j==1 or i==2 and j==2 or i==3 and j==1 or i==3 and j==3 or i==5 and j==5 or i==5 and j==7 or i==6 and j==6 or i==6 and j==7 or i==7 and j==7 or i==4 and j==1 or i==4 and j==2 or i==4 and j==3 or i==4 and j==4 or i==4 and j==5 or i==4 and j==6 or i==4 and j==7:
            print("*",end='\t')
        else :
            print("",end='\t')
    print("\n")