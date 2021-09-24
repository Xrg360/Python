# import os
# print(os.listdir())
# a=5
# b=6
# print(a//b)import os
import time
import os
os.system('cls')
print("hai")
print("your name - ")
name = input()
print("what is your age - ")
age = int(input())
if age>=10:
   
    print("hai "+name+" welcome to my Calculator \n\n\n\t\t\t\t\t loading......please wait")
    time.sleep(3)
        
    while True:
        os.system('cls')
        
        print("1.Add\n2.Sub\n3.multiply\n4.Divide\n0.EXIT")
        print("\nYOUR CHOICE - ")
        cho = int(input())
        if cho ==0:
            break            
        print("no - ")
        n1=input()
        print("no - ")
        n2=input()
    
        if cho==1:
            for i in range(5,0,-1):
             os.system('cls')
             print("sum of "+n1+" + "+n2+" = "+str(int(n1)+int(n2)))
             print("note down fast.... clearing in "+str(i)+"s")
             time.sleep(1)
        elif cho==2:                        
             for i in range(5,0,-1):
                os.system('cls')
                print("diference of "+n1+" - "+n2+" = "+str(int(n1)-int(n2)))
                print("note down fast.... clearing in "+str(i)+"s")
                time.sleep(1)
        elif cho==3:                        
            for i in range(5,0,-1):
             os.system('cls')
             print("Product of "+n1+" x "+n2+" = "+str(int(n1)*int(n2)))
             print("note down fast.... clearing in "+str(i)+"s")
             time.sleep(1)
        elif cho==4:                        
            for i in range(5,0,-1):
             os.system('cls')
             print(n1+"/"+n2+" = "+str(int(n1)/int(n2)))
             print("note down fast.... clearing in "+str(i)+"s")
             time.sleep(1)
 
else:
    print (name+" you are under age")