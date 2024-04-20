"""
************************************************************************
   Lab Exercise 2: Problem 3                                      
   Programmed By: Berongoy, Gerald S.                                       
   Course and Section: BSCpE 1-4                                                         
   Instructor: Prof. Julius S. Cansino                                                      
   Date Submitted:  March 24, 2024                                                     
************************************************************************
"""
myfile = open("integers.txt", "r") # Open the file "integers.txt" in read mode
squared = open("double.txt", "w") # Open the file "double.txt" in write mode
cube = open("cube.txt", "w") # Open the file "cube.txt" in write mode

# Iterate over each line in the file
for num in myfile:
    squared_line = int(num) ** 2 # Calculate the squared of the number
    squared.write(str(squared_line) + "\n") # Write the squared value to "double.txt" file
    cube_line = int(num) ** 3 # Calculate the cube of the number
    cube.write(str(cube_line) + "\n") # Write the cube value to "cube.txt" file

# Close the file "integers.txt"
myfile.close()
# Close the file "double.txt"
squared.close()
# Close the file "cube.txt"
cube.close()
