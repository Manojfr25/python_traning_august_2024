# Program to Find Sum of digits of a number

num = input('Enter a number to find the sum of digits: ')
sum=0

if num.isdigit():
    for i in num:
       sum+=int(i)
else:
    print('Input is not a valid number.')

print('Sum of digits of a number is', sum)