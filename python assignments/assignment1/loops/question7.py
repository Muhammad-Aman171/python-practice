
# 7. Find the factorial of a number using a while loop.

number = int(input("enter your number : "))
factorial = 1

for i  in range(1 , number + 1) :
    factorial *= i


print(factorial)