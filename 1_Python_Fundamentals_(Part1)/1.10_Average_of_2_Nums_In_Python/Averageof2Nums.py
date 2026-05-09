# WAP to find the average of two numbers
num1 = 10
num2 = 20
average = (num1 + num2) / 2
print("The average of", num1, "and", num2, "is:", average)
# output:
    # The average of 10 and 20 is: 15.0


# You can also take user input for the numbers to make the program more interactive:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
average = (num1 + num2) / 2
print("The average of", num1, "and", num2, "is:", average)
# output:
    # Enter the first number: 5
    # Enter the second number: 15
    # The average of 5.0 and 15.0 is: 10.0

# Notes:
# The average of two numbers is calculated by adding them together and dividing the sum by 2.
# In the second example, we use the `float()` function to convert the user input into floating-point numbers, allowing for decimal values.