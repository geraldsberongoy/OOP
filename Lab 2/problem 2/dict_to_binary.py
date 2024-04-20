import pickle

students = {
    "Anthony": 3.0,
    "Bennet": 2.3,
    "Koko": 1.3,
    "Yelan": 1.4,
    "Ren": 1.7,
    "Aether": 1.3,
    "Lumine": 1.3,
    "Franco": 2.9,
    "Nahida": 1.1,
    "Neuv": 1.2,
    "Ben": 1.6,
    "Jean": 1.2,
    "Diluc": 1.4,
    "Xiao": 1.6,
    "Yanfei": 1.8,
    "Ayaka": 1.3,
    "Ayato": 1.2,
    "Viola": 1.5,
    "Yen": 1.9,
    "Yuki": 1.9
}
# Save students dictionary to a binary file
save_binary = open('students.bin', 'wb')
pickle.dump(students, save_binary)
save_binary.close()