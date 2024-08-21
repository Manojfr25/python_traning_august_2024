# Program to print the Equi Lateral Triangle of N lines

n=int(input('Enter number of lines: '))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()