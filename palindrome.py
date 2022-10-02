#this program is to print the palindrome of a number
def palindrome(n):
    temp = n
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if temp == rev:
        return True
    else:
        return False
#driver code
n = int(input("Enter the number: "))
if palindrome(n):
    print("The number is palindrome")
else:
    print("The number is not palindrome")
    