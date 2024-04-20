string = input("Enter a string: ").lower()

sub = "aeious"
new_sub = "eioua$"
nums = "1234"
new_string = ""
for char in string:
    if char in sub:
        new_string += new_sub[sub.find(char)]
    elif char in nums:
        new_string += str(int(char)*2)
    else:
        new_string += char
print(new_string[0].upper() + new_string[1:])
 