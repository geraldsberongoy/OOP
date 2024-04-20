"""
************************************************************************
   Programmed By: Gerald S. Berongoy                                                     
   Course and Section: BSCpE 1-4                                                         
   Instructor: Prof. Julius S. Cansino                                                      
   Date Submitted:  March 09, 2024                                                    
************************************************************************
"""

# PROBLEM 1 – ENCRYPTION
# Write a Python Script that will accept a string as a plain text and then 
# the program will encrypt it using the following character substitute:
# 'a' = *, 'e' = &, 'i' = # , 'o' = + 'u' = !
# See sample output:
# Enter a string to encrypt: the quick brown fox jumps over the lazy dog.
# Encrypted string:th& q!#ck br+wn f+x j!mps +v&r th& l*zy d+g
separator = "*"*60
title = "Problem: 1"
author = "Gerald S. Berongoy"
print(f"{separator}\nProgram: {title}\nProgrammed by: {author}\n{separator}")
str_input = input("Enter a string to encrypt: ")
str_input = str_input.lower()

for i in str_input:
    if i == "a":
        str_input = str_input.replace(i, "*")
    elif i == "e":
        str_input = str_input.replace(i, "&")
    elif i == "i":
        str_input = str_input.replace(i, "#")
    elif i == "o":
        str_input = str_input.replace(i, "+")
    elif i == "u":
        str_input = str_input.replace(i, "!")

print(f"Encrypted string: {str_input}")