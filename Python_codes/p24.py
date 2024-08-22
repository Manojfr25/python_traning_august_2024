# Check if a number is Prime

num=int(input("Enter the number: "))
if num <= 1:
   print(num,"is not a Prime number")
if num % 2 != 0 or num % 3!=0 or num % 5 != 0:
   print(num,"is a Prime number")
   
# not completed yet