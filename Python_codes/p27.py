# Find Nth Fibo term (assume 1 and 2 as 1st 2 terms)

n=int(input("Enter the number: "))
a, b = 0, 1
if n==1:
   print(f"The 1th term of Fibonacci series is: 0")
elif n==2:
   print(f"The 2nd term of Fibonacci series is: 1")
elif n>2:
   for i in range(2,n+1):
       a, b = b, a + b
print(f"The {i}th term of Fibonacci series is: {b}")