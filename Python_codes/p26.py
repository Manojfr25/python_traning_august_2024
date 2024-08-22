# Find the Nth Prime number

N=int(input("Enter a number: "))
n=1000
prime_num_list=[]
i=6
if n < 1:
    print("Please enter a valid number")
elif n>=2:
    if n==2:
        prime_num_list.append(2)
    elif 3 <= n <= 4:
        prime_num_list.append(2)
        prime_num_list.append(3)
    elif 5 <= n <= 6:
        prime_num_list.append(2)
        prime_num_list.append(3)
        prime_num_list.append(5)
    elif n >=7:
        prime_num_list.append(2)
        prime_num_list.append(3)
        prime_num_list.append(5)
        prime_num_list.append(7)
        while i <= n:
            if i % 2 != 0 and i % 3 !=0 and i % 5 != 0 and i % 7 != 0:
               prime_num_list.append(i)
            i += 1
print(f"The {N}th prime number is: {prime_num_list[N+1]}")