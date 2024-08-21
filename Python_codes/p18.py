# Program to Find Odd placed Even digits in a number

input_number=int(input('Enter a Number :'))
num=str(input_number)
odd_placed_num=''
even_num=''
for i in range(len(num)+1):
    if i % 2 == 0:
        odd_placed_num+=num[i]
for j in odd_placed_num:
    if int(j) % 2 == 0:
        even_num+=j
print('Odd placed Even digits in',num,'is',even_num)