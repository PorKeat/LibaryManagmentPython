from app.admin.model.adminModel import AdminModel
from app.admin.view.adminView import AdminView
from app.admin.controller.adminController import AdminController
from app.auth.model.authModel import AuthModel
from app.auth.controller.authController import AuthController
from app.auth.view.authView import AuthView



userOne = AdminModel()
adminView = AdminView()
adminController = AdminController()
authModel = AuthModel()
authController = AuthController()
authView = AuthView()

# authView.login_role()
# authView.register_user()
adminView.show_all_user()

# adminView.found_user_by_id()
# adminView.updated_user()
adminView.upgrade_user()

# !ADMIN FEATURE

# TODO ListAllUser
# userOne.listUser()

# TODO Upgrade Role
# id = input("ID to upgrade role: ")
# role = int(input("Role[1.Admin 2.Librarian 3.Member]: "))
# userOne.upgradeRole(id=id,role=role)

# TODO Update
# id = int(input("ID to update: "))
# username = input("Username: ")
# first_name = input("FirstName: ")
# last_name = input("LastName: ")
# phone_number = input("PhoneNumber: ")
# userOne.updateUserData(username, first_name, last_name, phone_number, id)

# TODO Search
# print("""
#       [+] Search User 🔍
#       [1] Search user by id
#       [2] Search user by name
#       """)
# while True:
#     op = int(input("Choose your Option: "))
#     if op == 1:
#         id = int(input("Search ID: "))
#         userOne.searchUserByID(id)
#         break
#     elif op == 2:
#         name = input("Search Name: ")
#         userOne.searchUserByName(name)
#         break
#     else:
#         print("Invalid Input !")

# TODO Register
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
# while True:
#     phone_number = input("PhoneNumber: ")
#     if userOne.validatePhoneNumber(phone_number):
#         break
#     else:
#         print("Invalid Input !")
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

# TODO Login
# email = input("Email: ")
# password = getpass('Password: ')

# userOne.login(
#     email,
#     password
# )

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

