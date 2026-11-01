# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
name = input("Enter your name: ")
# TODO: Ask the user for their age and store it in a variable
age = input("Enter your age: ")
print(age)
# TODO: Print a greeting using the name and age variables
name = input("Enter your name: ")
age = input("Enter your age :")
print(f"hello {name}, you are {age} years old!")
#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
length = int(input("Enter the length of the rectangle: "))
# TODO: Ask the user for the width of a rectangle and store it as an integer
width = int(input("Enter the width of the rectangle:" ))
# TODO: Calculate the area of the rectangle
area = length * width
# TODO: Print the result
print(f"Area of rectangle is {area}")
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
celsius = float(input("Enter temperature in Celsius: "))
# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)
# TODO: Print the result rounded to two decimal places
fahrenheit = (celsius * 9/5) + 32
print(f"{fahrenheit:.2f}")