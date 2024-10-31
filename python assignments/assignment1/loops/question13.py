
# 13. Use nested loops to print a pyramid pattern of *.


count = 5

for i in range(1 , count + 1):
    print(" " * (count - i ) + "*" * (2 * i - 1))

