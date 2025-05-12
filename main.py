
print("Welcome to X calculator. Here, mathematics is our passion!")

valid_functions = ["+", "-", "*", "/"]

# Get the first number and convert it to float
first_number = float(input("Enter first number: "))
print("You have entered:", first_number)

# Get the operation
operation = input("Enter the function (+, -, *, /): ")

# Check if the function is valid
if operation not in valid_functions:
    print("The function entered is not in our supported functions.")
else:
    # Get the second number and convert to float
    second_number = float(input("Enter second number: "))

    # Perform the operation
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            result = "Error: Division by zero is not allowed."
        else:
            result = first_number / second_number

    # Display result
    print("Result:", result)
