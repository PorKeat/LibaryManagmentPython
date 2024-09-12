from app.admin.view.adminView import AdminView
from app.auth.view.authView import AuthView


adminView = AdminView()
authView = AuthView()



adminView.list_book()
adminView.change_genre()