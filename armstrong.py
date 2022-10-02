#this is to check whether the given number is armstrong or not
def armstrong(n):
    temp = n
    sum = 0
    while n > 0:
        dig = n % 10
        sum = sum + dig ** 3
        n = n // 10
    if temp == sum:
        return True
    else:
        return False
#driver code
n = int(input("Enter the number: "))
if armstrong(n):
    print("The number is armstrong")
else:
    print("The number is not armstrong")
# Compare this snippet from prime.py:
# #this program is to print the prime numbers between 1 to 100
# def prime(n):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         else:
#             return True
#     else:
#         return False
# #driver code
# for i in range(1, 101):
#     if prime(i):
#         print(i, end=' ')
# Compare this snippet from prime_rec.py:
# #this program is to print the prime numbers between 1 to 100 using recursion
# def prime(n, i):
#     if n <= 2:
#         if n == 2:
#             return True
#         else:
#             return False
#     if n % i == 0:
#         return False
#     if i * i > n:
#         return True
#     return prime(n, i + 1)
# #driver code
# for i in range(1, 101):
#     if prime(i, 2):
#         print(i, end=' ')