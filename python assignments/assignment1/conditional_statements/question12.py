
# 12. Write a program that takes a temperature in Celsius and
#  checks if it’s freezing, moderate, or hot.

temperature = int(input("enter your temperature in celsius : "))

if temperature >= 35 :
    print("the weather is hot")
elif temperature >= 15 and temperature <=34 :
    print("the weather is moderate")    
else:
    print("the weather is cold")    
    