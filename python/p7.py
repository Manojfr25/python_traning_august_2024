# Program to check if a number is Perfect Square

import math
number=int(input('Enter a number :'))
sqrt_num=math.sqrt(number)
if sqrt_num.is_integer():
   print(number,"is a perfect square.")
else:
    print(number,"is not a perfect square")