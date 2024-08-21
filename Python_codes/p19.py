# Program to print the Right angled Triangle of N lines

n=int(input('Enter number of lines: '))
for i in range(1, n+1):
    print('*' * i + ' ' * (n-i))