def split():
    global b_nm
    global a_nm
    global qty
    global price
    b_nm=[]
    a_nm=[]
    qty=[]
    price=[]
    with open("manager.txt") as f:
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