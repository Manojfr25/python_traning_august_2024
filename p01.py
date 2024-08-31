def find_factorial_iteretively(num):
    factorial_num = 1
    if num== 0 or num== 1: 
        return factorial_num
    for i in range(2, num-1):
        factorial_num *= i
    return factorial_num * num

def find_factorial_recursively(num):
    if num== 0 or num== 1: 
        return find_factorial_recursively(num-1)
    return find_factorial_recursively(num)
    
input_num = int(input('enter a number to find its factorial: '))
choice=int(input('1.iterative 2.recursive. your choice plz: '))

if choice==1: 
    print('The factorial of', input_num, 'is', find_factorial_iteretively(input_num))

elif choice==2:
    print('The factorial of', input_num, 'is', find_factorial_recursively(input_num))
   
