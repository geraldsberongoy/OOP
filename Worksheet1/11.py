print("""
************************************************************************
   Programmed By: Gerald S. Berongoy                                                     
   Course and Section: BSCpE 1-4                                                         
   Instructor: Prof. Julius S. Cansino                                                      
   Date Submitted:  March 16, 2024                                                    
************************************************************************
""")
string = input("Enter a string: ").lower()
nums = "1234"
substitution_dict = {'a': 'e', 'e': 'i', 'i': 'o', 
                     'o': 'u', 'u': 'a', "s": "$",
                     'b': 'c', 'c': 'd', 'd': 'f', 
                     'f': 'g', 'g': 'h', 'h': 'j', 
                     'j': 'k', 'k': 'l', 'l': 'm', 
                     'm': 'n', 'n': 'p', 'p': 'q', 
                     'q': 'r', 'r': 't', 't': 's', 
                     'u': 'v', 'v': 'w', 'w': 'x', 
                     'x': 'y', 'y': 'z', 'z': 'b', 
                     '5': '?', '6': '@', '7': '#', 
                     '8': '}', '9': '%', '0': '*'}

new_string = ""
for char in string:
    if char in substitution_dict:
        new_string += substitution_dict[char]
    elif char in nums:
        new_string += str(int(char)*2)
    else:
        new_string += char
new_string = (new_string[0].upper() + new_string[1:])[::-1]
print(new_string)

    
