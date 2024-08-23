# Program to Find odd placed digits in a number

input_number=int(input('Enter a Number :'))
odd_list=[]
while input_number != 0:
    digit = input_number % 10 # fetch last digit
    input_number = input_number // 100 #remove last 2 digit
    odd_list.append(digit)

print('Odd placed digits in',input_number,'is',odd_list)