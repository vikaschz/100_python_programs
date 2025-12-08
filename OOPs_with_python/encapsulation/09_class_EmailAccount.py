"""Design a class EmailAccount with private password.
Add methods to authenticate, change password, and block weak passwords."""

class EmailAccount:
    def __init__(self, password):
        self.__password = password

    def authenticate(self, password):
        return password == self.__password

    def change_password(self, old_password, new_password):
        if not self.authenticate(old_password):
            print("Authentication failed. Cannot change password.")
            return

        if len(new_password) < 6:
            print("Password too weak. Must be at least 6 characters.")
            return

        self.__password = new_password
        print("Password changed successfully.")

pass1 = EmailAccount("123456")
pass1.change_password("123456","654321")
pass1.authenticate("8585285")