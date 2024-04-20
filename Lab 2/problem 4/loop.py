number = open("integers.txt", "w")

for i in range(1, 21):
    number.write(str(i) + "\n")

number.close()