import os
def split():
    global b_nm
    global a_nm
    global qty
    global price
    b_nm=[]
    a_nm=[]
    qty=[]
    price=[]
    f_nm=input("Firstname - ")
    l_nm=input("Lastname  - ")
    t= t=f_nm+" - "+l_nm+" - issue"+".txt"
    try:
        with open(t) as f:
            lines=f.readlines()
            lines=[x.strip('\n') for x in lines]
            for i in range(len(lines)):
                index=0
                for a in lines[i].split(','):
                    if index==0:
                        b_nm.append(a)           
                    elif index==1:
                        a_nm.append(a)
                    elif index==2:
                        qty.append(a)
                    elif index==3:
                        price.append(a)
                    index+=1
    except:
        print("File not found")
    f.close()