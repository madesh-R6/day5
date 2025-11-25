import random
import string
def password_generator(length):
    characters = string.ascii_letters+string.digits+string.punctuation
    password="" 
    for i in range(length):
        password += random.choice(characters)
    return password
users_length = int(input("enter a password length:"))
print("your password is:",password_generator(users_length))