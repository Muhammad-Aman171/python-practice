
# check the number is prime or not :

userInput = int(input("enter your number : "))

if userInput <= 1:
    print("this number is smaller than 1")
else:    
    for i in range (2 , userInput):
        if userInput % i == 0:
            print("your number is not a prime number")
            break
    else:
        print("your number is a prime number")


