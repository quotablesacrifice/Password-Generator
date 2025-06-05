import random

print("Password: ")

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789-!@#$%^&*()?'

password = ''
for x in range(16):
    password += random.choice(chars)

print(password)