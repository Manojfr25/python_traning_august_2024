import pdb
pdb.set_trace()

def find_sum_of_digits(num):
    sum=0 
    while num != 0 :
        remainder = num%10
        num = num//10
        sum = sum + remainder
    return sum
input_num = int(input('enter a number to find the sum of digits'))
sum_of_digits = find_sum_of_digits(input_num)
print(f'sum of digits of {input_num} is {sum_of_digits}')