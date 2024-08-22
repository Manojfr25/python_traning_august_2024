# Print Prime numbers between M and N (M < N)

M=int(input("Enter Initial number: "))
N=int(input("Enter Final number: "))
if M<N: 
    i=M
    prime_num_list=[]
    while M <= i <= N:
        if i == 2 or i== 3 or i== 5 or i== 7 or i== 11 or i== 13:
            prime_num_list.append(i)
        elif i % 2 != 0 and i % 3 !=0 and i % 5 != 0 and i % 7 != 0 and i % 11 != 0 and i%13==0:
            prime_num_list.append(i)
        i += 1
    print(f"Prime number between {M} and {N} are: {prime_num_list}")
else: 
    print("Initial number should be less than Final number")