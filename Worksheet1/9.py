print("""
************************************************************************
   Programmed By: Gerald S. Berongoy                                                     
   Course and Section: BSCpE 1-4                                                         
   Instructor: Prof. Julius S. Cansino                                                      
   Date Submitted:  March 16, 2024                                                    
************************************************************************
""")
username = input("Enter your username: ")

if not username[0:4].isalpha():
    print("The first four characters must be letters.")
elif not username[4:6].isdigit():
    print("The last two characters must be digits.")
else:
    print("Your username", username, "is valid.")