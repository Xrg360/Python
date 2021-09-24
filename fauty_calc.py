print("1. Add\n2. Sub\n3. Mult\n4. div\n")
ch=int(input("choice - "))
if ch==1:
    a=int(input("number = "))
    b=int(input("number = "))
    if a==56 and b==9:
        print(a,"+",b,"= 77")
    else:
        print(a,"+",b,"=",a+b)
elif ch==2:
    a=int(input("number = "))
    b=int(input("number = "))
    print(a,"-",b,"=",a-b)
elif ch==3:
    a=int(input("number = "))
    b=int(input("number = "))
    if a==45 and b==3:
        print(a,"x",b,"= 555")
    else:
        print(a,"x",b,"=",a*b)
    
elif ch==4:
    a=int(input("number = "))
    b=int(input("number = "))
    if a==56 and b==6:
        print(a,"/",b,"= 4")
    else:
        print(a,"/",b,"=",a/b)
    

