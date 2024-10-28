
#7. Write a program to find the largest of three numbers.

userInput1 = int(input("enter fisrt number : "))
userInput2 = int(input("enter second number : "))
userInput3 = int(input("enter third number : "))

if userInput1 > userInput2 and userInput1 > userInput3 :
    print("first number is bigger ")
elif userInput2 > userInput1 and userInput2 > userInput3  :
    print("second number is bigger")
else :
    print("third number is bigger")

