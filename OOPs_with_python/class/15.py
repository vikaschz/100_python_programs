"""
15. Create a class Database that uses:
private data (__password)
method to update password
method to check access
"""

class Database:
    def __init__(self, password):
        # "Private" password (Python just name-mangles it)
        self.__password = password

    def update_password(self, old_pass, new_pass):
        if old_pass == self.__password:
            self.__password = new_pass
            print("Password updated successfully")
        else:
            print("Incorrect old password. Update failed.")

    def check_access(self, password):
        if password == self.__password:
            print("Access granted")
        else:
            print("Access denied")


# Example:
db = Database("admin123")

db.check_access("admin123")      # Access granted
db.update_password("admin123", "newpass321")
db.check_access("newpass321")    # Access granted
