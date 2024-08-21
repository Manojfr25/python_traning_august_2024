# Program to print X shape of N lines

n=int(input("Enter the number of lines: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j or i + j == n + 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()