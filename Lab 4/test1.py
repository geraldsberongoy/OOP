# Define custom exception
class FormulaError(Exception):
    def process_input(self, input_str):
        # Split the input string into elements
        elements = input_str.split()

        # Check if the input consists of 3 elements
        if len(elements) != 3:
            raise FormulaError("Input must consist of exactly 3 elements")
        else:
            return elements[0], elements[1], elements[2]

    def validate_elements(self, num1, operator, num2):
        if not num1.isdigit():
            raise FormulaError("First element must be a number.")
        elif not num2.isdigit():
            raise FormulaError("Third element must be a number.")
        elif operator not in ["+", "-"]:
            raise FormulaError("Second element must be '+' or '-'.")
        else:
            return float(num1), operator, float(num2)

def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    else:
        return num1 - num2
    
# Main program
try:
    # Get input from the user
    user_input = input("Enter 3 elements separated by spaces: ")

    # Create an instance of FormulaError class
    formula_error = FormulaError()

    # Process the input
    num1, operator, num2 = formula_error.process_input(user_input)
    
    # Validate the elements
    float_value1, operator, float_value2 = formula_error.validate_elements(num1, operator, num2)
    result = calculate(float_value1, operator, float_value2)
    print(result)
except FormulaError as e:
    # Handle FormulaError (custom exception)
    print(f"FormulaError: {e}")
