

userInput = int(input("enter your year : "))

if userInput % 4 == 0  or userInput % 100 == 0 or userInput % 400 == 0 :
    print( "this is a leap year")
else:
    print( "this is not a leap year")
