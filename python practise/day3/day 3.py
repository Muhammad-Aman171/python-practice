


# 5. Perfect Number Check:

# userInput = int(input("enter your number : "))
# total = 0
# for i in range(1 , userInput ):
#     if userInput % i == 0 :
#         total +=  i
#         print(i)
# if total == userInput :
#     print("this number is perfect number" , total)
# else:
#     print("this number is not perfect number" , total)



# Sum of Digits Until Single Digit:

# userInput = int(input("enter your number : "))

# strNum = str(userInput)
# total = 0
# for i in strNum:
#     total += int(i)
# print(total)


# Prime Factors: 

userInput = int(input("enter your number : "))

# primeFactorArr =  []

# if userInput > 0 :
#     for i in range(2 , userInput + 1):
#         if userInput % i == 0 :
#             print(i)
# else:
#     print("this number is nagetive ")


for i in range(2 , userInput + 1):
    total =   userInput / i
    if userInput >= total : 
        print(i)
    # else:
    #     print(i)    