import os
import ls
import datetime
import splitfori
import splitfori
def take_away():
    f_nm=input("Your firstname - ")
    l_nm=input("Your lastname - ")
    t=f_nm+" - "+l_nm+" - issue"+".txt"
    while True:
        splitfori.splitforissue(t)
        print("select - ")
        for i in range(len(ls.b_nm)):
            print(i," . ","to select ",ls.b_nm[i])
        print("100 . EXIT")
        a=int(input())
        if any(ls.b_nm[a] in word for word in splitfori.b_nm):
            print("You have the same book with you.....Please return it to continue")
            break
        else:
            q=int(input("quantity - "))
            if(int(ls.qty[a])>0):
                if(int(ls.qty[a])>=q):
                    ch=input("book is availible...Press y to issue book else press any key to continue and hit enter...!! ")
                    if(ch=='y'):
                        
                #______________________________________________________________________________________________________________________________________________________
                #        #         ind=splitfori.b_nm.index(ls.b_nm[a])zz        ----                                                                                  |
                #        #  splitfori.qty[ind]=int(splitfori.qty[ind])+1            |                                                                                 |
                #        #         with open(t,"w+") as fp:                           |                                                                                 |
                #        #             l=len(splitfori.b_nm)                         | ----------->this code needs to be rechecked that why it can't work              |
                #        #             if l==0:                                       |                                                                                 |
                #        #                 for i in range(1):                         |                                                                                 |
                #                                                                                                                                                       |
                #        #                     fp.write(splitfori.b_nm[i]+"   "+splitfori.a_nm[i]+"   "+str(splitfori.qty[i])+"   "+str(splitfori.price[i])+"\n")   |
                #        #             elif l!=0:                                                                                                                       |
                #        #                 for i in range(len(splitfori.b_nm)):                                                                                        |
                #        #                     fp.write(splitfori.b_nm[i]+"   "+splitfori.a_nm[i]+"   "+str(splitfori.qty[i])+"   "+str(splitfori.price[i])+"\n")   |
                #        #     else:                                                                                                                                    | 
                #_______________________________________________________________________________________________________________________________________________________|    
                        with open(t,"a+") as afp:
                            afp.write(ls.b_nm[a]+","+ls.a_nm[a]+","+str(q)+","+str(ls.price[a])+"\n")
                        ls.qty[a]=int(ls.qty[a])-q
                        with open("manager.txt","w+") as f:
                            for i in range(len(ls.b_nm)):
                                f.write(ls.b_nm[i]+","+ls.a_nm[i]+","+str(ls.qty[i])+","+str(ls.price[i])+"\n")
                        choice = input("to issue more books press y else press any key and hit enter...!!")
                        if choice=='y':
                            continue
                        else:
                            break
                    else:
                        return
                elif(int(ls.qty[a])<q):
                    print("Entered quantity of book not availible.......sorry for inconvinence caused.....!!!!")
                    continue
            elif(int(ls.qty[a])<=0):
                print("Book not availible.......sorry for inconvinence caused.....!!!!")
                
            elif(a==100):
                return
    f.close()
    afp.close()