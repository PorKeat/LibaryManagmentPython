from app.users.model.model import *
from getpass4 import getpass
import hashlib

userOne = UserModel() 

# userOne.register(
#     username="Demon",
#     first_name="De",
#     last_name="ReMon",
#     email="doremon@gmail.com",
#     password="Pass@12345",
#     phone_number="1234567890",
#     role=3
# )


# email = input("Email: ")
# password = getpass('Password: ')

# userOne.login(
#     email,
#     password
# )

# TODO Hashing Password
test=b"Pass@12345"
sha256 = hashlib.sha256()
sha256.update(test)
string_hash = sha256.hexdigest()
print(f"Hash:{string_hash}")
password = input("Password: ")
encoded_password = password.encode()
passWord = hashlib.sha256()
passWord.update(encoded_password)
hashedPass = passWord.hexdigest()
print(f"Hash:{hashedPass}")

