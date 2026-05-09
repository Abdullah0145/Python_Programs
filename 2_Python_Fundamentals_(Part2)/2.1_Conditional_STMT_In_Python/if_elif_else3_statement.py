# If-Elif-Else Statement in Python
# An if-elif-else statement is a conditional statement that allows you to execute one block of code if a certain condition is true, another block of code if another condition is true, and a final block of code if all conditions are false. The syntax for an if-elif-else statement in Python is as follows:
# if condition1:
#     # block of code to be executed if condition1 is true
# elif condition2:
#     # block of code to be executed if condition2 is true
# elif condition3:
#     # block of code to be executed if condition3 is true
# elif condition4:
#     # block of code to be executed if condition4 is true
# else:
#     # block of code to be executed if all conditions are false
# For example:
color = input("enter your traffic loight color: ")

if color == "red":
    print("Stop") # Output: Stop
elif color == "yellow":
    print("Ready") # Output: Ready
elif color == "green":
    print("Go") # Output: Go
else:
    print("Wrong color for traffic lights") # Output: Wrong color for traffic lights