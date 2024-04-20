"""
************************************************************************
   Lab Exercise 3                                      
   Programmed By: Berongoy, Gerald S.                                       
   Course and Section: BSCpE 1-4                                                         
   Instructor: Prof. Julius S. Cansino                                                      
   Date Submitted:  April 6, 2024                                                     
************************************************************************
"""

# Define a function to perform basic arithmetic operations
def calculator(operation, num1, num2):
    if operation == 1:
        return f"Result: {num1 + num2}"  # Addition
    elif operation == 2:
        return f"Result: {num1 - num2}"  # Subtraction
    elif operation == 3:
        return f"Result: {num1 * num2}"  # Multiplication
    elif operation == 4:
        try:
            return f"Result: {num1 / num2}"  # Division
        except ZeroDivisionError: # Handle division by zero error
            return "Error: Division by zero is not allowed!"

# Define function for input validation
def get_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Error: Please enter a valid number.")

# Define the main function
def main():
    print("\nWelcome to the Calculator Program\n")
    
    # Main loop to keep the program running until the user decides to exit
    while True:
        print("Enter operation:\n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division\n")

        try:
            # Prompt user to choose an operation
            operation = int(input("Choose an operation (1-4): "))
            if operation not in [1, 2, 3, 4]:
                print("\nInvalid operation. Choose between 1-4.\n")
                continue
            
            # Loop for inputting numbers and performing calculations
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            
            # Calculate and display result
            result = calculator(operation, num1, num2)
            print(result, "\n")
            
            # Check if the user wants to continue or exit
            if repeat() == False:
                break
                
        except ValueError:
            print("Error: Please enter a number only.\n")
            continue

# Function to ask the user if they want to continue
def repeat():
    while True:
        again = input("Do you want to try again? (yes/no): ")
        if again.lower() == "no":
            print("Thank you for using the Calculator 😊")
            return False
        elif again.lower() == "yes":
            main()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue

# Call the main function to start the program
main()