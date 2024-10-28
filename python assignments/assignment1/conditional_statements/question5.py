

# 5. Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).


userInput = int(input("enter your percentage : "))

if userInput > 100:
    print("Please enter your correct percentage")
elif userInput >= 90 :
    print("you got A+ grade")
elif userInput >= 80 and userInput < 90:
    print("you got A grade")
elif userInput >= 70 and userInput < 80:
    print("you got B grade")
elif userInput >= 60 and userInput < 70:
    print("you got C grade")
elif userInput >= 50 and userInput < 60:
    print("you got D grade")
elif userInput >= 40 and userInput < 50:
    print("you got D grade")
else:
    print("sorry, you are fail")
