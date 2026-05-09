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
# elif condition5:
#     # block of code to be executed if condition5 is true
# else:
#     # block of code to be executed if all conditions are false
# For example:
age = 100

if (age < 13):
    print("You are a child.") # Output: You are a child.
elif (age >= 13 and age < 18): #13 to 18
    print("you are a teenager.") # Output: you are a teenager.
elif (age >= 18 and age < 65): #18 to 65
    print("you are an adult.") # Output: you are an adult.
else:
    print("you are not a child, teenager, or adult.") # Output: you are not a child, teenager, or adult.