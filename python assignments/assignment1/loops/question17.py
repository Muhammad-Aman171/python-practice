
# 17. Write a program that continues to ask for a number until the correct number is guessed.


num = 3

while True : 
    guess = int(input('enter your number : '))

    if num == guess :
        print('congratulation! you guessed the number')
        break
    else:
        print('your number is wrong')
