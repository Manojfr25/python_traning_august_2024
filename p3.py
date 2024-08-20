# Accept a number as input ,say X & define a logic to get output Y.the input can be only 0 or 1 & output must be 1 if input is 0 & vice versa
X= int(input("Enter a number 0 or 1: "))
if X==0 or X==1:
  Y=1-X
  print('Input number:',X,',','Output number:',Y)
else:
  print('invalid input')
