import os
import inpusecurity
def func():
    print("hello")
os.system('cls')      
while True:
    print("please\n1.Signin\n2.Signup\n0.EXIT")
    cho=int(input())
    if cho==0:
        break
    if cho==1:
        usr=input("enter username - ")
        pas=input("enter pass - ")
        s=usr+":"+pas
        # print(s)
        
        with open("railmanage.txt") as f:
            toget= f.readlines()
            # print(toget)
            if any(s in word for word in toget):
                func()
            else:
                print("oops!!! retry")
    if cho==2:
        inpusecurity.inpufun()
                
            
            
      