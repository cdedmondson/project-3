import re


# Checks if user exists in database if not add user to database
def addUser(user, password):
    # If user name is not in database and the password is valid and the user id is valid then add new user
    if (not inDatabase(user)) and isValidPassword(password) and isValidUserID(user):
        database[user] = password
        names = open('names.txt', 'a')  # Open names file and set permissions to append
        codes = open('codes.txt', 'a')  # Open codes file and set permissions to append
        names.write(str("\n" + user))  # Add new user name to end of file
        codes.write(str("\n" + password))  # Add new password to end of file
        print(user, "was successfully added")
        names.close()  # Close file
        codes.close()  # Close file
        return True
    else:
        print(user, "already exists try another")
        return False


# Checks if user already exists in database or not
def inDatabase(new_user):
    if new_user in database:
        return True
    else:
        return False


# Count number of special characters and return count
def unique_special_count(password):
    # List of special characters
    special = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ '''
    return sum(ch in special for ch in list(password))


# Checks whether or not user name and password are valid
def isValidPassword(password):
    check = 1
    if len(password) >= 8:  # Make sure length of password is greater than 8 characters
        check += 1
    else:
        print("Password must be at least 8 characters long")
    if len(re.findall(r'[A-Z]', password)) >= 3:  # Make sure at least 3 characters are uppercase letters
        check += 1
    else:
        check -= 1
    if len(re.findall(r'[a-z]', password)) >= 3:  # Make sure at least 3 characters are lowercase letters
        check += 1
    else:
        check -= 1
    if len(re.findall(r'[0-9]', password)) >= 3:  # Make sure password contains at least 3 digits
        check += 1
    else:
        check -= 1
    if unique_special_count(password) >= 3 :  # Make sure password contains at least 3 symbols
        check += 1
    else:
        check -= 1
    if check == 4:  # If password passes all 4 or 5 tests return true else return false
        return True
    else:
        print("Password must contain at least 3 of the following conditions: 3 "
              "upper case letters, 3 lower case letters, 3 digits or 3 symbols")
        return False


# Check if user ID is valid
def isValidUserID(user_id):
    check = 0
    if user_id[0].isalpha():  # Check if first character is a letter
        check += 1
    else:
        print("First character of user id must contain letter")
    if any(char.isdigit() for char in user_id):  # Check if any digits exist is user id
        check += 1
    else:
        print("User id must contain both letters and digits")
    if check == 2:
        return True
    else:
        return False


# Check if login id and password match
def login(name, password):
    if inDatabase(name) and database[name] == password:
        print("Successfully logged-in:", name)
    else:
        print("Login id or password is not valid")


names = open('names.txt', 'r')  # Open names file and set permissions to read
codes = open('codes.txt', 'r')  # Open codes file and set permissions to read

names_list = names.read().splitlines()  # Read file line by line into names list
codes_list = codes.read().splitlines()  # Read codes line by line into codes list

database = dict(zip(names_list, codes_list))  # Save name as key and code as value into database

names.close()  # Close names file
codes.close()  # Close codes file

# Tests

# Add three new users
print("Test1")
addUser('Cameron123', 'HELloo##*')
addUser('Cameron111', 'HeLLoo123')
addUser('Cameron222', 'hELLoo#$@!')

# Login fail two users
print("Test2")
login('Cameron123', 'HELloo##12')
login('3333oYoY', 'yoyo33')

# Successfully login two users
print("Test3")
login('k3p124', 'kkkppp111_')
login('pizza3night', 'ddddDDDD1111')
