import os
import time
def inpufun():
    while True:
        os.system('cls')
        a=input("bookname - ")
        b=input("author name - ")
        c=input("quantity - ")
        d=input("price - ")
        with open ("manager.txt","a") as fp:
            fp.write(a+","+b+","+c+","+"$"+d+"\n")
        ch=input("do you want to add more books.....")
        if ch=='y':
            continue
        cho=input("do you want to see the input in file press y")
        if cho=='y':
            with open("manager.txt","r") as fp:
                os.system('cls')
                read=fp.read()
                print(read)
                time.sleep(1)
        else:
            return
    fp.close()
            # break
# inpufun()