
# 9. Write a program to print the first 10 Fibonacci numbers.

userInput = int(input("enter your number : "))

seq_fibanocci = [0 , 1 ]

for i in range(2 , userInput):
    fibonacci = seq_fibanocci[i - 1] + seq_fibanocci[i - 2]
    # print(fibonacci)
    seq_fibanocci.append(fibonacci)

print(seq_fibanocci)