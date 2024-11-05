# 1. write a program that check the number is positive, nagetive and zero

userInput = int(input("enter your number :"))

if userInput > 0 :
    print( "this number", userInput , "is positive")
elif userInput == 0 :
    print( "this number", userInput , "is equal to zero")
else:
    print( "this number", userInput , "is nagetive")
