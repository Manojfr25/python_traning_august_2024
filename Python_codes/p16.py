# Program to reverse a number

input_number=int(input('Enter a Number to reverse:'))
reversed_number=""
while input_number != 0:
    digit = input_number % 10 # fetch last digit
    input_number = input_number // 10 #remove last digit
    reversed_number += str(digit)
print("Reverse of a",str(input_number),'is',reversed_number)