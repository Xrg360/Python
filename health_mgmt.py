#this program is about health management system
def getDate():
    import datetime
    return datetime.datetime.now()
def fileHandle(name):
    while(True):
        filename=str(name+".txt")
        fp=open(filename,"a+")
        print("1. INSERT DATA \n2. RETRIVE DATA\n0. EXIT")
        ans=int(input("choice - "))
        if ans==1:
            print("1. EXCERCISE \n 2. FOOD\n")
            cho=int(input("Choice - "))
            if cho==1:
                excercise=input("name of excercise - ")
                ex=str(str(getDate())+" "+str(excercise))
                fp.writelines(ex)
                print("Record inserted succesfully ...")
            elif cho==2:
                diet=input("Diet - ")
                Diet = str(str(getDate())+" "+str(diet))
                fp.writelines(Diet)
                print("Record inserted succesfully ...")
            else:
                print("Enter a valid number..")
        elif ans==2:
            fp.seek(0)
            for lines in fp:
                print(lines+"\n")
        elif ans==0:
            break
        else:
            print("Enter a valid number..")
        fp.close()

while(True):
    print("Select Your Name - \n 1. Rohit\n 2. RG \n 3. Guest\n 0.EXIT")
    try:
        ch=int(input("Choice - "))
        if ch==1:
            fileHandle("Rohit")
        elif ch==2:
            fileHandle("RG")
        elif ch==3:
            fileHandle("Guest")
        elif ch==0:
            break
    except Exception as e:
        print(e)
