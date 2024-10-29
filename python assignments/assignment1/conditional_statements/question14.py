
# 14. Check if a year input by the user is a century year.

userInput = int(input("enter your year : "))

if userInput % 100 == 0:
    print("this year is century year")
else:
    print("this year is not a century year ")