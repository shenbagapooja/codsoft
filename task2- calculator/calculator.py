# Get two numbers from the user
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

# Get the operation from the user
op = input("Enter operation (+, -, *, /): ")

# Perform the calculation based on the operation
if op == '+':
    result = first + second
elif op == '-':
    result = first - second
elif op == '*':
    result = first * second
elif op == '/':
    if second == 0:
        result = "Error: Cannot divide by zero"
    else:
        result = first / second
else:
    result = "Invalid operation! Please use (+, -, *, /)"

# Display the result
print("Result:", result)
