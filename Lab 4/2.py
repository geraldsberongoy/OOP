def handle_file(file):
    print(f"Opening the '{file}'....")
    try:
        # Attempt to open the file in read mode
        with open(file, "r") as filename:
            # Read the contents of the file
            contents = filename.read()
            # Print the contents
            print("File contents:")
            print(contents)
            
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"FileNotFoundError: File '{file}' not found")
        
    except IOError:
        # Handle the case where an I/O error occurs during file reading
        print(f"IOError: Could not read file '{file}'.")
        
    finally:
        # Print a completion message regardless of success or failure
        print("File handling completed.\n")

def trigger_ioerror(file):
    print(f"Opening the '{file}'....")
    try:
        # Attempt to open the file in write mode
        with open(file, "w") as filename:
            filename.read() # trigger an I/O error by reading from a file opened in write mode
            
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"FileNotFoundError: File '{file}' not found.")
        
    except IOError:
        # Handle the case where an I/O error occurs during file writing
        print(f"IOError: Could not read file '{file}'.")
        
    finally:
        # Print a completion message regardless of success or failure
        print("File handling completed.\n")

# Case 1
file = "Lab 4/random.txt"
handle_file(file)  # Attempt to read an existing file

# Case 2
file = "Lab 4/nonexistent_file.txt" 
handle_file(file)  # Attempt to read a nonexxistent file

# Case 3
file = "Lab 4/sqrt_result.txt"
trigger_ioerror(file)  # Attempt to trigger an I/O error by writing to a file opened in read mode
