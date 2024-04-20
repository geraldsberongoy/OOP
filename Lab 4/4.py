def capitalize_last_name(fullname):
    """This function takes a full name as input and capitalizes the first name and uppercases the last name."""
    try:   
        if not isinstance(fullname, str):
             raise TypeError("Both parts of the name must be strings")
            
        fullname = fullname.split()
        
        # Checking if exactly two parts are provided
        if len(fullname) != 2:
            raise ValueError("You must enter exactly two parts of the name separated by a space")
               
        first_name = fullname[0]
        last_name = fullname[1]
        
        print(f"{first_name.capitalize()} {last_name.upper()}")
        
    except TypeError as e:
        print(f"TypeError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")

print("Case 1:")
capitalize_last_name(1000) #Test 1
print("\nCase 2:")
capitalize_last_name("john") #Test 2
print("\nCase 3:")
capitalize_last_name("Gerald Berongoy") #Test 3
print("\nCase 4:")
capitalize_last_name("Marc Talopi") #Test 4
