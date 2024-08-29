# Find sum of the series: 1 - n + n2 - n3 .... m terms

M=int(input("Enter Initial number: "))
N=int(input("Enter Final number: "))
if M<N:  
    n = float(M)
    term = (-M) ** N
    sum = (1 - term) / (1 + n)
    print(f"Sum of the series {M} and {N} terms is {sum}")
else:
   print("Initial number should be less than Final number")