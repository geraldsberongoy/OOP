def square_root(num):
    """Define square root of a number"""
    try:
        num = int(num)  
        if num < 0:
            raise ValueError("You can't find the square root of a negative number") 
        else:
            return num ** 0.5
    except ValueError as e:
        return f"ValueError: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"
    
def check_result(squared):
    """Check if the result is a digit and append it to a file"""
    if type(squared) is float or type(squared) is int:                                                           
        myfile = open("Lab 4/sqrt_result.txt", "w")
        myfile.write(str(squared) + "\n")
        myfile.close()
        print("Result saved to sqrt_result.txt")
    else:
        print(squared)
        
# Main program
num = input("Enter a number: ")
squared = square_root(num)
check_result(squared)




