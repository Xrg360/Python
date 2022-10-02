#this program is to find the matrix multiplication
def matrix_mul(a, b):
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] += a[i][k] * b[k][j]
    return c
#driver code
a = [[]]
b = [[]]
n=int(input("Enter the number of rows and columns: "))
print("Enter the elements of first matrix: ")
for i in range(n):
    for j in range(n):
        a[i][j] = int(input())
print("Enter the elements of second matrix: ")
for i in range(n):
    for j in range(n):
        b[i][j] = int(input())
print("The product of the two matrices is: ")
for i in range(n):
    for j in range(n):
        print(matrix_mul(a, b)[i][j], end=' ')
    print()
