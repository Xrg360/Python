import os
import ls
import datetime
import cust_split
def take_away():
    f_nm=input("Your firstname - ")
    l_nm=input("Your lastname - ")
    t=f_nm+" - "+l_nm+" - issue"+".txt"
    while True:
        cust_split.splitforissue(t)
        print("select - ")
        for i in range(len(cust_split.b_nm)):
            print(i," . ","to return ",cust_split.b_nm[i])
        print("100 . EXIT")
        a=int(input())
        q=int(input("quantity - "))
        if(int(cust_split.qty[a])>0):
            if(int(cust_split.qty[a])>=q):
                ch=input("Do you really want to return this book....(y/n)")
                if(ch=='y'):   
                    with open("manager.txt","w+") as wfp:
                        indx=ls.b_nm.index(cust_split.b_nm[a])
                        ls.qty[indx]=int(ls.qty[indx])+q
                        for i in range(len(ls.b_nm)):
                            wfp.write(ls.b_nm[i]+","+ls.a_nm[i]+","+str(ls.qty[i])+","+str(ls.price[i])+"\n")
                        
                        
                    cust_split.qty[a]=int(cust_split.qty[a])-q
                
                    with open(t,"w+") as f:
                            for i in range(len(cust_split.b_nm)):
                                f.write(cust_split.b_nm[i]+","+cust_split.a_nm[i]+","+str(cust_split.qty[i])+","+str(cust_split.price[i])+"\n")
                    choice = input("to return more books press y else press any key and hit enter...!!")
                    if choice=='y':
                        continue
                    else:
                        break
                else:
                    return
            elif(int(cust_split.qty[a])<q):
                print("Entered quantity of book not availible.......PLease check Again.....!!!!")
                continue
        elif(int(cust_split.qty[a])<=0):
            print("Book not availible.......sorry for inconvinence caused.....!!!!")
            
        elif(a==100):
            return