import os
import time
import ls
import issue
import inpu
import display
import cust_split
import custo_rec
import returning

os.system("cls")
ch = int(input("you want to continue as - \n1. Admin\n2.Customer\n"))
if ch == 1:
    inpu.inpufun()
elif ch == 2:
    os.system("cls")
    while True:
        print(
            "1. ISSUE BOOK\n"
            "2. CHECK AVAILIBILITY\n"
            "3. GET YOUR RECORD\n"
            "4. RETURN\n"
            "0. EXIT\n"
            "your choice - "
        )
        cho = int(input())
        if cho == 0:
            break
        elif cho == 1:
            ls.split()
            issue.take_away()
        elif cho == 2:
            ls.split()
            display.disp()
        elif cho == 3:
            cust_split.split()
            custo_rec.record()
        elif cho==4:
            ls.split()
            returning.take_away()
else:
    print("no valid input....")

