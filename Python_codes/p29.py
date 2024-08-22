# Find sum of the series: n + n(2) + n(3) + ..... m terms

M=int(input("Enter Initial number: "))
N=int(input("Enter Final number: "))
if M<N:  
   sum = M * N * (N + 1) // 2
   print(f"Sum of the series {M} and {N} terms is {sum}")
else:
   print("Initial number should be less than Final number")