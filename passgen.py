import random
import os

config_file = "config.txt"

file_path = ""

if os.path.exists(config_file):
    try:
        with open(config_file, 'r') as f:
            file_path = f.read().strip()
        print(f"Using saved password file path: {file_path}")
    except IOError:
        print(f"Error reading from {config_file} Please enter the path manually.")
        file_path = input("Please enter the full file path for your passwords.txt here:")
        try:
            with open(config_file, 'w') as f:
                f.write(file_path)
            print(f"New pass word file path saved: {file_path}")
        except IOError:
            print(f"Error saving new file path to {config_file} the path will not be remebered.")

else:
    file_path = input("Before continuing, somewhere on your computer, please create a .txt document for your passwords to be stored in." \
    "\nPlease enter the full file path for the .txt that you created: ")
    try:
        with open(config_file, 'w') as f:
            f.write(file_path)
        print(f"File path saved for future use: {file_path}")
    except IOError:
        print(f"Error saving the path to {config_file}. The path will not be remebered.")

what_password_for = input("What's this password for? ") # what service, app, etc. the password is for

print("Password: ")

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789-!@#$%^&*()?' #characters for the generator to choose from

password = ''
for x in range(16): # 16 char password
    password += random.choice(chars) # choosing random chars from chars string

print(password)

try:
    with open(file_path, 'a') as file: # appends or creates a file then appends with future generated passwords
        file.write(what_password_for + ":\n" + password + "\n\n") # appends the file with the service name and the password
    print(f"Password successfully appended to: {file_path}") # append successful

except IOError:
    print(f"An errer occured when attempting to write to the file: {file_path}") # append failed

input("\nPress Enter to exit...")