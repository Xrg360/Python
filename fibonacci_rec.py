#fibonacci series using recursion
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)\
#driver code
n = int(input("Enter the number of terms: "))
for i in range(n):
    print(fib(i), end=' ')
#output
# Enter the number of terms: 10
# 0 1 1 2 3 5 8 13 21 34
