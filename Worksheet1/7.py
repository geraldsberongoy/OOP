print("""
************************************************************************
   Programmed By: Gerald S. Berongoy                                                     
   Course and Section: BSCpE 1-4                                                         
   Instructor: Prof. Julius S. Cansino                                                      
   Date Submitted:  March 16, 2024                                                    
************************************************************************
""")

username = input("Enter your username with 6 character long: ")
if len(username) != 6:
    print("Your username must be 6 characters long. Please try another.")
else:
    print("Your username", username, "is valid.")