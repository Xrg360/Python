import os
import time
def func():
    print("hello")     
os.system('cls')      
while True:
    print("please\n1.Signin\n2.Signup")
    cho=int(input())
    if cho==1:
        usr=input("enter username - ")
        pas=input("enter pass - ")
        s=usr+pas
        # print(s)
        tosearch= open("railmanage.txt")
        for a in tosearch:
            if s in a:
                func()
                x=a
                break
        for a in tosearch:
            if x not in a:
                print("oops!!!")
                
                
                
            # print(toget)      ---
            # s in toget          |
            # my_set = set(a)     |          
            # a=toget             |-----> this is only aplicable           
            # if 's' in toget:    |       for any list
            #     func()        ---
        # print(s)
        # if s in f:
        #     func()
        #     s=toget
            
            
            
        # with open("railmanage.txt") as f:
        #     if s not in f:
        #         print("oops!!!")
        
            # elif s not in a:            ----------------->this cannot be implemented as
            #     print("oops!! invalid credential")      x will not be initialised if s not in a                              
            
    # elif cho==2:
    #      name=input("hai\nplease enter your username - ")
    #      os.system('cls')
    #      chk=input("Hey!! "+name+" do you want to continue to the authorization process(y/n)- ")
    #      if chk == "y":
    #          age=int(input("What's your age - "))
    #          passw = input("enter a password - ")
    #          with open("manage.txt","a") as f:
    #              f.write(name+passw+"\n")
    #          print("Authorizing you in .....Sit back and relax..")
    #          time.sleep(2)
    #          temp_nm=input("please enter your username - ")
    #          temp_pass=input("please enter your password - ")
    #      if(temp_nm == name and temp_pass == passw):
    #          print("authorizing......please wait...")
    #          time.sleep(2)
    #          print("succecfully created the identity with name "+name)
    #          time.sleep(4)
    #          func()
    #      else:
    #          print("incorrect credentials")
    # elif cho==0:
    #      break

               
    