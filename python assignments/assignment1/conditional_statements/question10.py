
# 10. Write a program to determine if a given character is a vowel or consonant.

userInput = input("enter your alphabet : ")

if userInput in ('a', 'A',  'e',  'E',  'i', 'I', 'o' , 'O' , 'u','U'  ):
    print("your enter alphabet is vowel")
else:
    print("your enter alphabet is consonant")    