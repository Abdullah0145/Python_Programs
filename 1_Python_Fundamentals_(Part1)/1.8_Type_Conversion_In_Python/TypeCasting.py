# Type Casting in Python
# Type casting, also known as type conversion, is the process of converting a value from one data type to another. In Python, you can perform type casting using built-in functions.
# The most common type casting functions in Python are:
# int() - converts a value to an integer
# float() - converts a value to a float
# str() - converts a value to a string
# bool() - converts a value to a boolean
# Example of type casting
# Converting a string to an integer
x = "10"
y = int(x)
print(y)  # Output will be 10
# Converting a string to a float
x = "10.5"
y = float(x)
print(y)  # Output will be 10.5
# Converting an integer to a string
x = 10
y = str(x)
print(y)  # Output will be "10"
# Converting a float to a string
x = 10.5
y = str(x)
print(y)  # Output will be "10.5"
# Converting a string to a boolean
x = "True"
y = bool(x)
print(y)  # Output will be True
# Converting an empty string to a boolean
x = ""
y = bool(x)
print(y)  # Output will be False
# Converting a non-empty string to a boolean
x = "Hello"
y = bool(x)
print(y)  # Output will be True
# Note: When converting a string to a boolean, any non-empty string will be considered True, while an empty string will be considered False.
# It's important to be cautious when performing type casting, as it can lead to unexpected results if the value being converted is not compatible with the target data type. Always ensure that the value you are trying to convert can be successfully cast to the desired type to avoid errors.
# Example of an error during type casting
x = "abc"
y = int(x)  # This will raise a ValueError
print(y)
# In this example, trying to convert the string "abc" to an integer will raise a ValueError because "abc" cannot be interpreted as a number. Always make sure to handle such cases appropriately in your code to prevent crashes.

# You can also use the type() function to check the data type of a variable before performing type casting.
x = "10"
print(type(x))  # Output will be <class 'str'>
y = int(x)
print(type(y))  # Output will be <class 'int'>

# In summary, type casting is a powerful feature in Python that allows you to convert values between different data types. It is essential to understand how to use type casting effectively to ensure that your code runs smoothly and handles data correctly. Always be mindful of the data types you are working with and the potential implications of type casting in your programs.

# You can also perform implicit type conversion, where Python automatically converts one data type to another when necessary. For example, when you add an integer and a float, Python will automatically convert the integer to a float before performing the addition.
x = 10
y = 10.5
z = x + y  # Python automatically converts x to a float before performing the addition
print(z)  # Output will be 20.5
# In this example, the integer 10 is implicitly converted to a float before being added to 10.5, resulting in a float output of 20.5. Implicit type conversion can be convenient, but it's important to be aware of it to avoid unintended consequences in your code.

# In conclusion, understanding type casting and type conversion in Python is crucial for writing effective and error-free code. Whether you are performing explicit type casting using built-in functions or relying on implicit type conversion, being mindful of data types and how they interact can help you avoid common pitfalls and ensure that your programs run smoothly. Always test your code to verify that type conversions are working as expected and handle any potential errors gracefully.

# You can also create custom type conversion functions if you need to convert between data types in a specific way that is not covered by the built-in functions. For example, you might want to convert a string representation of a date into a datetime object.
from datetime import datetime

def convert_to_datetime(date_string, format_string):
    return datetime.strptime(date_string, format_string)
# Example usage of the custom type conversion function
date_string = "2024-06-01"
format_string = "%Y-%m-%d"
datetime_object = convert_to_datetime(date_string, format_string)
print(datetime_object)  # Output will be 2024-06-01 00:00:00
# In this example, the convert_to_datetime function takes a date string and a format string as input and uses the datetime.strptime method to convert the string into a datetime object. This allows you to work with dates in a more structured way in your code. Custom type conversion functions can be very useful when you need to handle specific data formats or perform complex conversions that are not covered by the built-in functions.

# In summary, type casting and type conversion are essential concepts in Python that allow you to work with different data types effectively. Whether you are using built-in functions for explicit type casting, relying on implicit type conversion, or creating custom type conversion functions, understanding how to manage data types is crucial for writing robust and error-free code. Always be mindful of the data types you are working with and test your code to ensure that type conversions are functioning as expected.

# It's also worth noting that Python provides a way to check if a value can be converted to a specific type before attempting the conversion. This can help you avoid errors and handle exceptions gracefully.
def is_convertible_to_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
# Example usage of the is_convertible_to_int function
value = "123"
if is_convertible_to_int(value):
    print(f"{value} can be converted to an integer.")
else:
    print(f"{value} cannot be converted to an integer.")
value = "abc"
if is_convertible_to_int(value):
    print(f"{value} can be converted to an integer.")
else:
    print(f"{value} cannot be converted to an integer.")
# In this example, the is_convertible_to_int function checks if a given value can be converted to an integer by attempting the conversion and catching any ValueError exceptions that may occur. This allows you to safely check for convertibility before performing the actual type casting, which can help prevent errors in your code.
# In conclusion, type casting and type conversion are fundamental concepts in Python that enable you to work with different data types effectively. By understanding how to use built-in functions for explicit type casting, relying on implicit type conversion, creating custom type conversion functions, and checking for convertibility, you can write robust and error-free code that handles data types appropriately. Always be mindful of the data types you are working with and test your code to ensure that type conversions are functioning as expected.

# You can also use the isinstance() function to check the type of a variable before performing type casting. This can help you ensure that you are working with the expected data types and avoid errors.
x = "10"
if isinstance(x, str):
    print(f"{x} is a string.")
    # Now you can safely convert it to an integer if needed
    if is_convertible_to_int(x):
        x = int(x)
        print(f"Converted {x} to integer.")
else:
    print(f"{x} is not a string.")
# In this example, we first check if the variable x is a string using the isinstance() function. If it is a string, we then check if it can be converted to an integer using the is_convertible_to_int() function before performing the conversion. This approach helps ensure that we are working with the expected data types and can prevent errors in our code.
# In summary, using the isinstance() function in conjunction with type casting can help you write safer and more robust code by ensuring that you are working with the expected data types before performing any conversions. Always be mindful of the data types you are working with and test your code to ensure that type conversions are functioning as expected.

# In addition to the built-in type casting functions, Python also provides a way to define custom classes and implement type conversion methods. This allows you to create your own data types and specify how they should be converted to other types.
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def __str__(self):
        return f"{self.celsius}°C"
# Example usage of the Temperature class
temp = Temperature(25)
print(temp)  # Output: 25°C
print(temp.to_fahrenheit())  # Output: 77.0°F
# In this example, we define a Temperature class that has a method to convert the temperature from Celsius to Fahrenheit. We also implement the __str__ method to provide a string representation of the temperature. This allows us to create instances of the Temperature class and perform type conversions as needed.
# In conclusion, Python's type casting and type conversion capabilities are versatile and allow you to work with different data types effectively. Whether you are using built-in functions for explicit type casting, relying on implicit type conversion, creating custom type conversion functions, checking for convertibility, or defining custom classes with type conversion methods, understanding how to manage data types is crucial for writing robust and error-free code. Always be mindful of the data types you are working with and test your code to ensure that type conversions are functioning as expected.

# Notes:
# - Type casting is the process of converting a value from one data type to another.
# - Python provides built-in functions for type casting, such as int(), float(), str(), and bool().
# - Implicit type conversion occurs when Python automatically converts one data type to another when necessary.
# - Custom type conversion functions can be created to handle specific data formats or complex conversions.
# - The isinstance() function can be used to check the type of a variable before performing type casting.
# - Always be mindful of the data types you are working with and test your code to ensure that type conversions are functioning as expected.
# - Type casting can lead to errors if the value being converted is not compatible with the target data type, so it's important to handle such cases appropriately in your code.
# - Understanding type casting and type conversion is essential for writing effective and error-free code in Python.