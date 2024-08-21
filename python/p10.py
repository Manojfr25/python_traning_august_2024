# Program to check if the alphabet is Vowel or Consonant

str_alphabet =input("Enter a alphabet : ")
if len(str_alphabet) == 1 and str_alphabet.isalpha() == True:
    if str_alphabet.lower() in ['a', 'e', 'i', 'o', 'u'] :
            print(str_alphabet, "is a Vowel.")
    else :
            print(str_alphabet , "is a Consonant.")
else :
        print("Invalid input! Please enter a single alphabet.")