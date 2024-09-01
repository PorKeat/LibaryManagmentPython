username = input("Username: ")
first_name = input("First Name: ")
last_name = input("Last Name: ")
while True:
    email = input("Email: ")
    if userOne.validateEmail(email):
        break
    else:
        print("Invalid Input Email!")
while True:
    password = getpass('Password: ')
    if userOne.validatePass(password):
        break
    else:
        print("Invalid Input Password!")
while True:
    phone_number = input("PhoneNumber: ")
    if userOne.validatePhoneNumber(phone_number):
        break
    else:
        print("Invalid Input !")
while True:
    role = int(input("Role [1.Admin 2.Librarian 3.Member]: "))
    if role in [1, 2, 3]:
        break
    else:
        print("Please enter a valid number for role (1, 2, 3)")
    
userOne.register(
    username,
    first_name,
    last_name,
    email,
    password,
    phone_number,
    role
)