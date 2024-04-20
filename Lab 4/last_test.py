# Define custom exception
class FormulaError(Exception):
    pass

def process_input(input_str):
    elements = input_str.split()
    if len(elements) != 3:
        raise FormulaError("Input must consist of exactly 3 elements")
    else:
        return elements

def validate_elements(elements):
    num1, operator, num2 = elements
    try:
        float_value1 = float(num1)
        float_value2 = float(num2)
    except ValueError:
        raise FormulaError("First and third element must be numbers.")
    if operator not in ["+", "-"]:
        raise FormulaError("Second element must be '+' or '-'.")
    return float_value1, operator, float_value2

def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    else:
        return num1 - num2

# Main program
while True:
    user_input = input("Enter 3 elements separated by spaces (or 'quit' to exit): ")
    if user_input.lower() == "quit":
        break
    try:
        elements = process_input(user_input)
        float_value1, operator, float_value2 = validate_elements(elements)
        result = calculate(float_value1, operator, float_value2)
        print(result)
    except FormulaError as e:
        print(f"FormulaError: {e}")
