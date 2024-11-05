
# 4. Print the multiplication table of a given number.

count = int(input("enter your number : ")) 

for i in range(1 , int(input("enter your range : ")) + 1 ):
    total =  count * i 
    print (count , "x" , i , "=" , total)
