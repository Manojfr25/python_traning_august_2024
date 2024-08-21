# Program to find Sum of even(odd) digits in a number

input_number=int(input('Enter a Number sum of even numbers:'))
sum=0
while input_number != 0:
    digit = input_number % 10 # fetch last digit
    input_number = input_number // 10 #remove last digit
    if digit % 2 == 0:
        sum += digit
print("sum of even digit numbers is",sum)