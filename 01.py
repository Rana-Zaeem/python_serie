
# Python Basics

# Print a message to the console
print("Hello, World!")

# Variables and data types
name = "Alice"  # String
age = 25        # Integer
height = 5.6    # Float
is_student = True  # Boolean

# Basic arithmetic operations
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# Conditional statements
if age > 18:
  print(f"{name} is an adult.")
else:
  print(f"{name} is a minor.")

# Loops
# For loop
for i in range(5):
  print(f"Iteration {i}")

# While loop
count = 0
while count < 3:
  print(f"Count is {count}")
  count += 1

# Functions
def greet(person):
  return f"Hello, {person}!"

print(greet(name))

# Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print("Fruits:", fruits)

# Dictionaries
person = {"name": "Alice", "age": 25, "is_student": True}
print("Person's name:", person["name"])

# Exception handling
try:
  result = a / 0
except ZeroDivisionError: 
  print("Cannot divide by zero!")