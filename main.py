from app.auth.view.authView import AuthView
import os


authView = AuthView()

if __name__ == "__main__":
    os.system("cls")
    authView.normal_user()
