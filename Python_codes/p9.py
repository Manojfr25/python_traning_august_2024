# Program to Print Math table of a number

num=int(input('Enter a number to print its Math table: '))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")