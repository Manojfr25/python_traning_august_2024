# Program to accept 3 distinct number & find smallest number 
'''numbers=[]
for i in range(3):
   print('Enter number',str(i),': ')
   x=int(input())
   numbers.append(x)
numbers.sort()
print('Smallest number is: ',numbers[0])'''
input_num1 = int(input('Enter first number'))
input_num2 = int(input('Enter second number'))
input_num3 = int(input('Enter third number'))
if input_num1<input_num2 and input_num1<input_num3:
    print(input_num1 , 'is the smallest number')
elif input_num2<input_num3 and input_num2<input_num1:
    print(input_num2 , 'is the smallest number')
elif input_num3<input_num2 and input_num3<input_num1:
    print(input_num3 , 'is the smallest number')