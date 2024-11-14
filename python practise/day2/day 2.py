
# 1. check the number is prime or not :

# userInput = int(input("enter your number : "))

# if userInput <= 1:
#     print("this number is smaller than 1")
# else:    
#     for i in range (2 , userInput):
#         if userInput % i == 0:
#             print("your number is not a prime number")
#             break
#     else:
#         print("your number is a prime number")



# 2. please make your Fibonacci series : 

# userInput = int(input("enter your number : "))

# num = [0 , 1]

# for i in range(2 , userInput):
#     num.append(num[-1] + num [-2])

# print(num)




# 3. Factorial Calculation:


# userInput = int(input("enter your number : "))

# num = 1
# for i in range( 1, userInput + 1):
#     num *= i
#     print(num)


# 4.  Armstrong Number Check:

# num = int(input("enter your number : "))
# str_num = str(num)
# len_num = len(str_num)

# total = sum(int(digits) ** len_num for digits in str_num )
# if total == num :
#     print(total,  "is Armstrong number")
# else:
#     print( total, "  is not Armstrong number" )


# 5. Perfect Number Check:


userInput = int(input("enter your number : "))
total = 0
for i in range(1 , userInput ):
    if userInput % i == 0 :
        total +=  i
        print(i)
if total == userInput :
    print("this number is perfect number" , total)
    print(i)
else:
    print("this number is not perfect number" , total)





















# def is_armstrong(num):
#     num_str = str(num)
#     num_length = len(num_str)
#     total = sum(int(digit) ** num_length for digit in num_str)
#     return total == num

# number = int(input("Enter a number: "))
# if is_armstrong(number):
#     print("It's an Armstrong number.")
# else:
#     print("It's not an Armstrong number.")
