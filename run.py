from app.admin.view.adminView import AdminView
from app.auth.view.authView import AuthView
from app.member.view.memberView import MemberView


adminView = AdminView()
authView = AuthView()
memberView = MemberView()



# adminView.list_book()
# adminView.change_genre()
memberView.list_book()