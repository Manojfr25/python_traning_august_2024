# Program to find 2nd smallest digit in a number

smallest = 9
second_smallest = 9
num = input("Enter a number: ")
for i in range(len(num)):
    if int(num[i]) < smallest:
        smallest = int(num[i])
    else:
        pass
for i in range(len(num)):
    if int(num[i]) < second_smallest and int(num[i]) != smallest:
        second_smallest = int(num[i])
    else:
        pass

print("Second smallest digit in the number is:", second_smallest)