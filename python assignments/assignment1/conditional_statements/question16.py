
# 16. Take the length of three sides and classify the
#  triangle (equilateral, isosceles, or scalene).

side1 = float(input("enter your first side : "))
side2 = float(input("enter your second side : "))
side3 = float(input("enter your third side : "))


if side1 == side2 == side3 :
    print ("this triangle is equilateral")
elif side1 == side2 or side2 == side3 or side3 == side1  :
    print("this triangle is isosceles")  
else :
    print ("this triangle is scalene ")