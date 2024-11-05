
# 13. Take two numbers and an operator (+, -, *, /) as input
#  and perform the corresponding operation.


num1 = float(input("enter first number : "))
operator = input("enter your operator : ")
num2 = float(input("enter second number : ")) 

if operator == '+' :
    print(num1 + num2)
elif operator == '-'  :  
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else :
    print("you does not enter your operator")                
