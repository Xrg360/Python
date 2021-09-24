import os
import ls
import pandas
def disp():
    os.system('cls')
    for _ in range (len(ls.b_nm)):
        data = [ls.b_nm,ls.a_nm,ls.qty,ls.price]
    headers=["BOOKNAME - ", "AUTHOR/PUBLISHER - ", "QUANTITY - ", "PRICE - "] 
    print(pandas.DataFrame(data,headers))
    print("\n\n")
    # print("Bookname\t   "+"Authorname\t   "+"Quantity\t   "+"Price\t   \n")
    # for i in range(len(ls.b_nm)):
    #     print(ls.b_nm[i],"            ",ls.a_nm[i],"                 ",ls.qty[i],"                        ",ls.price[i],"\n")
    