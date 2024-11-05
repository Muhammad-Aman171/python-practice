
# 2. write a program that give the input from the user and tell 
# that the user are senior citizen, adult and minor age.

userInput = int(input("enter your age : "))

if userInput >= 50 :
    print( "you are a senior citizen")
elif userInput >= 18 and userInput <=49 :
    print( "you are a Adult")
else:
    print( "your look like a minor age")
