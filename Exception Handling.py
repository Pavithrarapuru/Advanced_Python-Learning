# EXCEPTION HANDLING

# Exception . An exception is an event occurs during the code execution time and will disrupts the normal flow of a program.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")



# Try

try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")

# Specific Exception Handling

try:
    number = int("abc")

except ValueError:
    print("Invalid value")    

# Multiple EXCEPT Blocks
try:
    number = int(input("Enter number: "))
    result = 100 / number

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero") 

# We can store the Exception Object as e
try:
    result = 10 / 0

except ZeroDivisionError as e:
    print(e)
print(type(e))
print(e)           


# ELSE
try:
    result = 10 / 2

except ZeroDivisionError:
    print("Division error")

else:
    print("Result:", result)

# FINALLY

try:
    result = 10 / 2

except ZeroDivisionError:
    print("Error")

finally:
    print("Execution completed")    

# raise ( The raise statement iss used when a developer manually raise an exception in the code)

age = 15

if age < 18:
    raise ValueError("Age must be 18 or above")