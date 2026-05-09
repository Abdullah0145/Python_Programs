# Taking User Input in Python
name = input("What is your name? ")
print("Hello, " + name + "!")
# Taking numerical input
age = int(input("How old are you? "))
print("You are " + str(age) + " years old.")
# Taking multiple inputs
num1, num2 = map(int, input("Enter two numbers separated by space: ").split())
print("The sum of the numbers is: " + str(num1 + num2))
# Taking float input
height = float(input("What is your height in meters? "))
print("You are " + str(height) + " meters tall.")
# Taking boolean input
is_student = input("Are you a student? (yes/no) ").lower() == "yes"
print("Student status: " + str(is_student))
# Taking list input
fruits = input("Enter your favorite fruits separated by commas: ").split(",")
print("Your favorite fruits are: " + ", ".join(fruits))
# Taking dictionary input
person_info = input("Enter your name and age separated by a comma: ").split(",")
person = {"name": person_info[0], "age": int(person_info[1])}
print("Person information: " + str(person))
# Taking multiple lines of input
print("Enter your address (press Enter twice to finish):")
address = []
while True:
    line = input()
    if line:
        address.append(line)
    else:
        break
print("Your address is:")
for line in address:
    print(line)
# output:
    # What is your name? John
    # Hello, John!
    # How old are you? 25
    # You are 25 years old.
    # Enter two numbers separated by space: 5 10
    # The sum of the numbers is: 15
    # What is your height in meters? 1.75
    # You are 1.75 meters tall.
    # Are you a student? (yes/no) yes
    # Student status: True
    # Enter your favorite fruits separated by commas: apple,banana,orange
    # Your favorite fruits are: apple, banana, orange
    # Enter your name and age separated by a comma: Alice,30
    # Person information: {'name': 'Alice', 'age': 30}
    # Enter your address (press Enter twice to finish):
    # 123 Main St
    # Anytown, USA

    # Your address is:
    # 123 Main St
    # Anytown, USA
    # Note: The above code demonstrates various ways to take user input in Python, including strings, integers, floats, booleans, lists, dictionaries, and multiple lines of input.

# Notes: 
# Always remember to handle user input carefully, especially when expecting specific data types, to avoid errors and ensure a smooth user experience.
# Additionally, consider using try-except blocks to handle potential exceptions that may arise from invalid input.