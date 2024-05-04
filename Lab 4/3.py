# Define custom exception
class FormulaError(Exception):
    """Raise for specific Formula error."""

def process_input(input_str):
    """Process the input string and return the elements."""
    elements = input_str.split()
    if len(elements) != 3:
        raise FormulaError("Input must consist of exactly 3 elements")
    else:
        return elements[0], elements[1], elements[2]
    
def validate_elements(num1, operator, num2):
    """Validate the elements and return the float values."""
    try:
        float(num1)
        float(num2)
    except ValueError:
        raise FormulaError("First and third elements must be numbers.")
    if operator not in ["+", "-", "*", "/"]:
        raise FormulaError("Operator must be one of '+', '-', '*', '/'")
    return float(num1), operator, float(num2)

def calculate(num1, operator, num2):
    """Define the calculation based on the operator."""
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return num1 / num2
    
# Main program
while True:
    user_input = input("Enter 3 elements separated by spaces (or 'quit' to exit): ")
    if user_input.lower() == "quit":
        print("Exiting the program...Goodbye!")
        break  
    try:
        num1, operator, num2 = process_input(user_input)
        float_value1, operator, float_value2 = validate_elements(num1, operator, num2)
        result = calculate(float_value1, operator, float_value2)
        print("Result: ", result, "\n")
    except FormulaError as e:
        print(f"FormulaError: {e}")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    finally:
        print("Running again...")