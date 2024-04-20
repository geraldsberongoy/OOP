print("""
************************************************************************
   Programmed By: Gerald S. Berongoy                                                     
   Course and Section: BSCpE 1-4                                                         
   Instructor: Prof. Julius S. Cansino                                                      
   Date Submitted:  March 16, 2024                                                    
************************************************************************
""")
letter = input("Enter a letter: ")

if letter.islower():
    print("The letter is lowercase.")
elif letter.isupper():
    print("The letter is uppercase.")