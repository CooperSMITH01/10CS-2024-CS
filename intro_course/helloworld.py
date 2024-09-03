# Variables
# Variables are used to store data in a program.
# In python, variables are created by assigning a value to a meaningful name.
# The value of a variable can be changed or updated throughout the program.
# Variables contain one type of data at a time, but the data type can change.
# Data types in Python include integers, floats, strings, and booleans.
'''
name = "Fred" # this variable contains a string 'str' which (text)
age = 15 # this variable contains an integer 'int' which is a whole number
salary = 1000.50 # this variable contains a float 'float' which is a decimal number
is_student = True #
'''

name = input("Enter your name: ") # this variable contains a string 'str' which (text)
age = int(input("Enter your age: ")) # this variable contains an integer 'int' which is a whole number
salary = float(input("Enter your salary: ")) # this variable contains a float 'float' which is a decimal number
is_student = bool(input("Are you a student? (True/False): ")) #

print(type(name))
print(type(age))
print(type(salary))
print(type(is_student))
print("Name: ", name)

if is_student == True:
    student = "Yes"
else:
    student = "No"

# the following is an F-string
print(f"{name} is {age} years old and earns $ {salary} per month. Is he a student? {is_student}")

print(f"{name} is {age} years old and earns $ {salary}0 per month. Is he a student {student}")

