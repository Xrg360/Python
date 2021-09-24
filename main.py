import os
import time
os.system('cls')
print("hai")
print("your name - ")
name = input()
print("what is your age - ")
age = int(input())
if age>=10:
   
    print("hai "+name+" welcome to Calculator \n\n\n\t\t\t\t\t loading......please wait")
    time.sleep(3)
        
    while True:
        os.system('cls')
        
        print("1.Add\n2.Sub\n3.multiply\n4.Divide\n0.EXIT")
        print("\nYOUR CHOICE - ")
        cho = int(input())
        if cho==1:
            print("no - ")
            n1=input()
            print("no - ")
            n2=input()
            for i in range(5,0,-1):
             os.system('cls')
             print("sum of "+n1+"+ "+n2+" = "+str(int(n1)+int(n2)))
             print("note down fast.... clearing in "+str(i)+"s")
             time.sleep(1)
        elif cho==2:                        
            print("no - ")
            n1=input()
            print("no - ")
            n2=input()
            for i in range(5,0,-1):
             os.system('cls')
             print("diference of "+n1+"- "+n2+" = "+str(int(n1)-int(n2)))
             print("note down fast.... clearing in "+str(i)+"s")
             time.sleep(1)
        elif cho==3:                        
            print("no - ")
            n1=input()
            print("no - ")
            n2=input()
            for i in range(5,0,-1):
             os.system('cls')
             print("Product of "+n1+" x "+n2+" = "+str(int(n1)*int(n2)))
             print("note down fast.... clearing in "+str(i)+"s")
             time.sleep(1)
        elif cho==4:                        
            print("no - ")
            n1=input()
            print("no - ")
            n2=input()
            for i in range(5,0,-1):
             os.system('cls')
             print(n1+"/"+n2+" = "+str(int(n1)/int(n2)))
             print("note down fast.... clearing in "+str(i)+"s")
             time.sleep(1)
        if cho ==0:
            break            
    
 
else:
    print (name+" you are under age")