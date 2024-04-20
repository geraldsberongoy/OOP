"""
************************************************************************
   Programmed By: Gerald S. Berongoy                                                     
   Course and Section: BSCpE 1-4                                                         
   Instructor: Prof. Julius S. Cansino                                                      
   Date Submitted:  March 09, 2024                                                    
************************************************************************
"""

# PROBLEM 2 –DECRYPTION
# Write a Python Script that will accept a string as encrypted text and then 
# the program will decrypt it using thefollowing character substitute:
# 'a' = *, 'e' = & , 'i' = # , 'o' = + 'u' = !

# See sample output:
# Enter a string to decrypt: th& q!#ck br+wn f+x j!mps +v&r th& l*zy d+g.
# The Plain Text:the quick brown fox jumps over the lazy dog.

str_input = input("Enter a string to decrypt: ")
str_input = str_input.lower()
for i in str_input:
    if i == "*":
        str_input = str_input.replace(i, "a")
    elif i == "&":
        str_input = str_input.replace(i, "e")
    elif i == "#":
        str_input = str_input.replace(i, "i")
    elif i == "+":
        str_input = str_input.replace(i, "o")
    elif i == "!":
        str_input = str_input.replace(i, "u")
print("Decrypted string:", str_input)

