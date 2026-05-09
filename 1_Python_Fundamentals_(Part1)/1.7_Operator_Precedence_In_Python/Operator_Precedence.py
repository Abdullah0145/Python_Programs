# Operator Precedence in Python
# Operator precedence determines the order in which operations are evaluated in an expression.
# In Python, the operator precedence is as follows (from highest to lowest):
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Unary operators +, -
# 4. Multiplication *, Division /, Floor Division //, Modulus %
# 5. Addition +, Subtraction -
# 6. Comparison operators ==, !=, <, >, <=, >=
# 7. Logical operators not
# 8. Logical operators and
# 9. Logical operators or
# Example to demonstrate operator precedence
result = 3 + 4 * 2 / (1 - 5) ** 2
print(result)  # Output will be 3.5
# In this example, the operations are evaluated in the following order:
# 1. Parentheses: (1 - 5) is evaluated first, resulting in -4
# 2. Exponentiation: (-4) ** 2 is evaluated next, resulting in 16
# 3. Multiplication and Division: 4 * 2 is evaluated, resulting in 8, and then 8 / 16 is evaluated, resulting in 0.5
# 4. Addition: Finally, 3 + 0.5 is evaluated, resulting in 3.5
# To change the order of operations, you can use parentheses to group expressions as needed.
# For example:
result = (3 + 4) * 2 / (1 - 5) ** 2
print(result)  # Output will be 7.0
# In this case, the operations are evaluated in the following order:
# 1. Parentheses: (3 + 4) is evaluated first, resulting in 7
# 2. Parentheses: (1 - 5) is evaluated next, resulting in -4
# 3. Exponentiation: (-4) ** 2 is evaluated, resulting in 16
# 4. Multiplication and Division: 7 * 2 is evaluated, resulting in 14, and then 14 / 16 is evaluated, resulting in 0.875

# It's important to understand operator precedence to ensure that your expressions are evaluated in the way you intend. Always use parentheses to clarify the order of operations when necessary.

# You can also use the built-in function `help()` to get more information about operator precedence in Python:
help("operator precedence")
# This will display the operator precedence table and provide more details about how operators are evaluated in Python.

# In summary, understanding operator precedence is crucial for writing correct and efficient code in Python. Always be mindful of the order in which operations are evaluated and use parentheses to ensure that your expressions are evaluated as intended.

# You can also use the `ast` module to parse expressions and analyze operator precedence programmatically. This can be useful for more complex expressions or when you want to create a custom expression evaluator.
import ast
expression = "3 + 4 * 2 / (1 - 5) ** 2"
tree = ast.parse(expression, mode='eval')
print(ast.dump(tree, indent=4))
# This will show the abstract syntax tree (AST) of the expression, which can help you understand how the expression is structured and how operator precedence is applied.

# Notes:
# - Always remember to use parentheses to clarify the order of operations when necessary.
# - Be aware of the operator precedence rules to avoid unexpected results in your expressions.
# - Use the `help()` function to get more information about operator precedence in Python.
# - The `ast` module can be used to analyze expressions and understand operator precedence programmatically.
# By mastering operator precedence, you can write more efficient and correct code in Python.