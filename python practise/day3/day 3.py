


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

primeFactorArr =  []

for i in range(2 , userInput + 1):
    while userInput % i == 0 :
        primeFactorArr.append(i)
        userInput = userInput // i







# # User se ek number input lena
# num = int(input("Enter a number to find its prime factors: "))

# print("Prime factors are:", end=" ")

# # 2 se √num + 1 tak range define karte hain
# for factor in range(2, int(num**0.5) + 1):
#     # Jab tak num ko factor se divide kar sakte hain
#     while num % factor == 0:
#         print(factor, end=" ")
#         num = num // factor  # num ko factor se divide karte raho

# # Agar num ab bhi 1 se bara hai, toh woh khud ek prime factor hai
# if num > 1:
#     print(num)
