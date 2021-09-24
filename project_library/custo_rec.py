import os
import pandas
import cust_split
def record():
    os.system('cls')
    for _ in range (len(cust_split.b_nm)):
        data = [cust_split.b_nm,cust_split.a_nm,cust_split.qty,cust_split.price]
    headers=["BOOKNAME - ", "AUTHOR/PUBLISHER - ","QUANTITY - ","PRICE - "] 
    print(pandas.DataFrame(data,headers))
    print("\n\n")