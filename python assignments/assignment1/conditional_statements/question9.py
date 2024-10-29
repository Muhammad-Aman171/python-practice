

# 9. Take three sides of a triangle as input and check if they form a valid triangle

side1 = input("enter your side1 length : ")
side2 = input("enter your side2 length : ")
side3 = input("enter your side3 length : ")


if (side1 + side2) > side3 and  (side1 + side3) > side2 and  (side2 + side1) > side1 :
    print("this triangle is valid form")
else:
    print("this triangle is not valid form")    