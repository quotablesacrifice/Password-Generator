import random

what_password_for = input("What's this password for? ") #what service, app, etc. the password is for

print("Password: ")

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789-!@#$%^&*()?' #characters for the generator to choose from

password = ''
for x in range(16): # 16 char password
    password += random.choice(chars) # choosing random chars from chars string

print(password)

file_path = "your .txt path" # if you have an existing .txt, use an absolute path if .txt is in a different directoy from the script. 
                                  # if .txt is in a parent directory for the folder the script is in, use '../' to go up one dir. can be used as many times as needed.
                                  # if theres no existing .txt, a new one will be created within the same folder as the script

try:
    with open(file_path, 'a') as file: # appends or creates a file then appends with future generated passwords
        file.write(what_password_for + ":\n" + password + "\n\n") # appends the file with the service name and the password
    print(f"Password successfully appended to: {file_path}") # append successful

except IOError:
    print(f"An errer occured when attempting to write to the file: {file_path}") # append failed