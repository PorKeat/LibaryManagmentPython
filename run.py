from app.admin.view.adminView import AdminView
from app.auth.view.authView import AuthView
from app.member.view.memberView import MemberView


adminView = AdminView()
authView = AuthView()
memberView = MemberView()



authView.normal_user()
# adminView.list_user()
