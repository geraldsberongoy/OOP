"""
************************************************************************
   Lab Exercise 2: Problem 2                                            
   Programmed By: Berongoy, Gerald S.                                       
   Course and Section: BSCpE 1-4                                                         
   Instructor: Prof. Julius S. Cansino                                                      
   Date Submitted:  March 24, 2024                                                     
************************************************************************
"""
import pickle

# Load students dictionary from the binary file
load_binary = open('students.bin', 'rb')
students = pickle.load(load_binary)

# Print the students dictionary
for names,key in students.items():
    print(names,key)

# Close the file
load_binary.close()


highest_gwa = float('inf')  # Initialize to positive infinity
highest_name = None # Initialize to None

# Iterate through the students dictionary to find the student with the highest GWA
for name, gwa in students.items():
    if gwa < highest_gwa:
        highest_gwa = gwa
        highest_name = name

# Print the student with the highest GWA
print('The student with the highest GWA is {} with a GWA of {}'.format( highest_name, highest_gwa))
