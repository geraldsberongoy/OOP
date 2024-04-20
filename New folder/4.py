# Open the file containing integers for reading
myfile = open("integers.txt", "r")
# Open the file for doubled integers for writing
double = open("double.txt", "w")
# Open the file for cubed integers for writing
cube = open("cube.txt", "w")

# Iterate through each line in the input file
for num in myfile:
    # Convert the number to an integer and double it
    double_line = int(num) * 2
    # Write the doubled number to the double file, followed by a newline
    double.write(str(double_line) + "\n")
    # Calculate the cube of the number
    triple_line = int(num) ** 3
    # Write the cubed number to the cube file, followed by a newline
    cube.write(str(triple_line) + "\n")

# Close the input and output files
myfile.close()
double.close()
cube.close()
