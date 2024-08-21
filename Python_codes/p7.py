# Program to check if a number is Perfect Square

number=int(input('Enter a number :'))
sqrt_num=number ** 0.5
sqrt_num= float(sqrt_num)
real_num = sqrt_num*sqrt_num
if real_num == number:
    print(number,"is a perfect square.")
else:
    print(number,"is not a perfect square")