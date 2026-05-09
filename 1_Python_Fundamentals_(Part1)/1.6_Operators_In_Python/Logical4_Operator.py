# Logical Operators in Python
# The logical operators in Python are used to combine conditional statements.
# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Returns True if the statement is not true
## 1. not ##
var = False
print (not var) #true 

var1 = False
print(not (5 > 8)) #true

## 2. and ##
var = False
print ((5 > 3) and (3 > 2)) #True 

var = False
print((5 > 3 and (3 > 8))) #False 

# 3. OR 
var = False
print((5 > 3 and (3 > 8))) #True 

var = False
print((5 > 13 and (3 > 8))) #False