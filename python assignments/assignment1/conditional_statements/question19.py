
# 19. Check if a string input is uppercase, lowercase, or a mix.

userInput = input("enter your string : ")

if userInput.islower():
    print("your string is lowercase")
elif userInput.isupper() :
    print("your string is uppercase")
else:
    print("your string is a mix up of lowercase and uppercase")

