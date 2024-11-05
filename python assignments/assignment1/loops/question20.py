
# 20. Create a program that simulates a countdown timer starting from a given number down to zero.

import time

user_input = int(input("enter your number : "))

print("timer is start")

for i in range( user_input ,0, -1 ):
    print(i)
    time.sleep(1)

print("timer is finished")

