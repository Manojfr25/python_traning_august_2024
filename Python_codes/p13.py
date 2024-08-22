# Program to find smallest digit in a number

smallest = 9
num = input("Enter a number: ")
for i in range(len(num)):
    if int(num[i]) < smallest:
        smallest = int(num[i])
    else:
        pass
print("Smallest digit in the number is:", smallest)