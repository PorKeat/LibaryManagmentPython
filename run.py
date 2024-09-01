from app.users.model.model import *
from getpass4 import getpass
import hashlib

userOne = UserModel() 

# username = input("Username: ")
# first_name = input("First Name: ")
# last_name = input("Last Name: ")
# while True:
#     email = input("Email: ")
#     if userOne.validateEmail(email):
#         break
#     else:
#         print("Invalid Input Email!")
# while True:
#     password = getpass('Password: ')
#     if userOne.validatePass(password):
#         break
#     else:
#         print("Invalid Input Password!")
# phone_number = input("PhoneNumber: ")
# while True:
#     role = int(input("Role [1.Admin 2.Librarian 3.Member]: "))
#     if role in [1, 2, 3]:
#         break
#     else:
#         print("Please enter a valid number for role (1, 2, 3)")
# userOne.register(
#     username,
#     first_name,
#     last_name,
#     email,
#     password,
#     phone_number,
#     role
# )


email = input("Email: ")
password = getpass('Password: ')

userOne.login(
    email,
    password
)

# TODO Hashing Password
# test=b"Pass@12345"
# sha256 = hashlib.sha256()
# sha256.update(test)
# string_hash = sha256.hexdigest()
# print(f"Hash:{string_hash}")
# password = input("Password: ")
# encoded_password = password.encode()
# passWord = hashlib.sha256()
# passWord.update(encoded_password)
# hashedPass = passWord.hexdigest()
# print(f"Hash:{hashedPass}")

