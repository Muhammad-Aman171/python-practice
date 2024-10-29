
# 17. Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.

enterInteger = int(input("enter your integer : "))

if enterInteger % 2 == 0:
    print("this number is multiple of 2")
elif enterInteger % 3 == 0:
    print("this number is multiple of 2")
elif enterInteger % 2 == 0 and enterInteger % 3 == 0:
    print("this number is multiple of both")
else:
    print("this number is not multiple of both number")
