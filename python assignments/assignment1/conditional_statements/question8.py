
# 8. Create a program that checks if a given string is a palindrome.

string = input("enter your string : ")
is_palindrome = True

for i in range(len(string) // 2 ):
    if string[i] != string[len(string) - i - 1 ]:
        is_palindrome = False 
    break

if is_palindrome :
    print("string is palindrome")
else :
    print("string is not palindrome")




# this code is made by chatgpt but I can also understand thier code