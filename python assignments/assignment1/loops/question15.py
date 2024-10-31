
# 15. Print the sum of even and odd numbers separately up to a given number.


numbers = int(input("enter your number : "))

even_num = 0
odd_num = 0

for i in range(1 , numbers + 1):
    if i % 2 == 0 :
        even_num += i
    else:
        odd_num +=i 

print(" the sum of even numbers : " , even_num)
print(" the sum of odd numbers : " , odd_num)





