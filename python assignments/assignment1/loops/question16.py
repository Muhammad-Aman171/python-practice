
# 16. Create a program to calculate the sum of the digits of an inputted integer.

userInput = str(int(input("enter your number : ")))
sum_number = 0

for i in userInput:
    sum_number +=  int(i)

print(sum_number )