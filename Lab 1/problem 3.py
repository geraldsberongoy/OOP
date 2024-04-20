"""
************************************************************************
   Programmed By: Gerald S. Berongoy                                                     
   Course and Section: BSCpE 1-4                                                         
   Instructor: Prof. Julius S. Cansino                                                      
   Date Submitted:  March 09, 2024                                                    
************************************************************************
"""
# Write a program that asks the user for the plaintext (all uppercase letters, no  spaces)  
# and  the  keyword  (all  uppercase  letters)  and  produce  the ciphertext using the Vigenère cipher. 
# Give the output of your program for the following message and key:
# Message: THISISTHELASTTASKHOORDAY
# Key: KNIGHTS

def char_to_num(text):
    converted_list = []
    for char in text:
        for keys, value in dict_map.items():
            if keys == char:
                converted_list.append(value)
    return converted_list

def num_to_char(text):
    result = []
    for chars in text:
        for keys, value in dict_map.items():
            if value == chars:
                result.append(keys)
    return result

message = str(input("Enter a message: ").upper().replace(" ", ""))
key = str(input("Enter a key: ").upper()).replace(" ", "")
len_message = len(message)
len_key = len(key)

letter_a_to_z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dict_map= {}

for index in letter_a_to_z:
    dict_map.update({index:letter_a_to_z.find(index)})
    
if not len_message == len_key:
    key_fill = ""
    for index in range(len_message):
        key_fill += key[index % len_key]
    key = key_fill

message_cipher = char_to_num(message)
key_cipher = char_to_num(key)

add_list = [sum(i) for i in zip(message_cipher, key_cipher)]
mod_list = [i % 26 for i in add_list]
result = num_to_char(mod_list)

print("Message:", *message_cipher)
print("Key:", *key_cipher)
print("Ciphered Text: ", *result)
