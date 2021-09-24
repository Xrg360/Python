import os
import time
os.system('cls')
name=input("hai\nplease enter your name - ")
os.system('cls')
chk=input("Hey!! "+name+" do you want to continue to the authorization process(y/n)- ")
if chk == "y":
    age=int(input("What's your age - "))
    if age>15:
        passw = input("enter a password - ")
        print("Authorizing you in .....Sit back and relax..")
        time.sleep(4)
        temp_nm=input("please enter your username - ")
        temp_pass=input("please enter your password - ")
        if(temp_nm == name and temp_pass == passw):
            print("authorizing......please wait...")
            time.sleep(4)
            print("succecfully created the identity with name "+name)
        else:
            print("incorrect credentials")
    else:
        print("under age....")        
else:
    print("Thanks for been here....")