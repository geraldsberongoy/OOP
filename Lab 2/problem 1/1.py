"""
************************************************************************
   Lab Exercise 2: Problem 1                                               
   Programmed By: Berongoy, Gerald S.                                       
   Course and Section: BSCpE 1-4                                                         
   Instructor: Prof. Julius S. Cansino                                                      
   Date Submitted:  March 24, 2024                                                     
************************************************************************
"""

# Open the file "numbers.txt" in read mode
numbers = open("numbers.txt", "r")
# Open the file "even.txt" in write mode
even = open("even.txt", "w")
# Open the file "odd.txt" in write mode
odd = open("odd.txt", "w")

# Iterate through each line in the "numbers" file
for num in numbers:
    if int(num) % 2 == 0: # Check if the number is even
        even.write(num) # Write the even number to the "even" file
    elif int(num) % 2 != 0: # If the number is not even, it must be odd
        odd.write(num) # Write the odd number to the "odd" file

numbers.close() # Close the "numbers" file

even.close() # Close the "even" file

odd.close() # Close the "odd" file


