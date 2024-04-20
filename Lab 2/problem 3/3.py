"""
************************************************************************
   Lab Exercise 2: Problem 3                                      
   Programmed By: Berongoy, Gerald S.                                       
   Course and Section: BSCpE 1-4                                                         
   Instructor: Prof. Julius S. Cansino                                                      
   Date Submitted:  March 24, 2024                                                     
************************************************************************
"""
myfile = open("myfile.txt", "a") # Open the file in append mode and assign it to myfile

# Function to enter lines into the file
def enter():
    line = input("Enter line: ") # Prompt the user to enter a line
    myfile.write(line + "\n") # Write the entered line to the file
    loop()# Call the loop function to check if there are more lines to enter

# Function to loop and continue entering lines if the user chooses to
def loop():
    while True:
        yes_no = input("Are there more lines y/n? ") # Ask the user if there are more lines to enter
        if yes_no.lower() == "n":  # If the user enters 'n', close the file and return from the loop
            myfile.close()
            return
        elif yes_no.lower() == "y": # If the user enters 'y', call the enter function to enter another line
            enter()
            return
        else: # If the user enters neither 'y' nor 'n', prompt them to enter again
            print("Please enter 'y' or 'n'.")

# Call the enter function to start entering lines into the file
enter()

