import os
def inpufun():
    os.system('cls')
    a=input("please input a username - ")
    b=input("please input password - ")
    with open ("railmanage.txt","a") as fp:
        fp.write(a+":"+b+"\n")
    with open("railmanage.txt","r") as fp:
        read=fp.read()
        print(read)