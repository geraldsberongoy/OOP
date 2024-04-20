"""
************************************************************************
   Programmed By: Gerald S. Berongoy                                                     
   Course and Section: BSCpE 1-4                                                         
   Instructor: Prof. Julius S. Cansino                                                      
   Date Submitted:  March 09, 2024                                                    
************************************************************************
"""
# Problem #4:Counting them all!!!!
# Write a program that will ask the user to enter a string of any number of  characters.  
# Then the  program  will outputon  the  screen  the following count of characters based on the entered string:

# Sample Run:The quick brown fox jumps 44 times over the lazy 3 dogs!!!!
# Number of vowels:13
# Number of consonants:28
# Numbers of digits:3
# Number of Special characters(including the spaces):15
# Total number of characters found on the string:59

string = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
special = 0
total = 0

for i in string:
    if i in "aeiouAEIOU":
        vowels += 1
    elif i.isalpha():
        consonants += 1
    elif i.isdigit():
        digits += 1
    else:
        special += 1
    total += 1
    
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")
print(f"Numbers of digits: {digits}")
print(f"Number of Special characters(including the spaces): {special}")
print(f"Total number of characters found on the string: {total}")