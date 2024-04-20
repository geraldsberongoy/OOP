print("""
************************************************************************
   Programmed By: Gerald S. Berongoy                                                     
   Course and Section: BSCpE 1-4                                                         
   Instructor: Prof. Julius S. Cansino                                                      
   Date Submitted:  March 16, 2024                                                    
************************************************************************
""")

name = input("Enter your name: ")

def lower(name):
    return name.lower()
def upper(name):
    return name.upper()
def first_letter_upper(name):
    return name[0].upper() + name[1:].lower()

print("Lowercase:", lower(name))
print("Uppercase:", upper(name))
print("First letter upper:", first_letter_upper(name))
