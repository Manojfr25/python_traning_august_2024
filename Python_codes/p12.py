# Program to Find count of digits of a number

input_num = input("Enter a number to count digits of a number: ")

if input_num.isdigit():
    count = len(input_num)
    print("Number of digits in the given number:", count)