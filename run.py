from app.admin.model.adminModel import AdminModel
from app.admin.view.adminView import AdminView
from app.admin.controller.adminController import AdminController
from app.auth.model.authModel import AuthModel
from app.auth.controller.authController import AuthController
from app.auth.view.authView import AuthView


adminView = AdminView()
authView = AuthView()



adminView.list_user()
authView.login()