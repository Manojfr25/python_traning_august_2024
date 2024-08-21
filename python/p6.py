# Program to check if the alphabet is uppercase

user_input = input("Enter a alphabet or a word : ")
if user_input.isupper():
    print(user_input, "is an uppercase alphabet")
else:
    print(user_input,"is not an uppercase alphabet")