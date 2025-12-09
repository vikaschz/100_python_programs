"""Create a class HospitalPatient with private medical record data.
Allow access only to authenticated users (simulate authentication).
Log all access through an internal method."""


class HospitalPatient:
    def __init__(self, name, record):
        self.name = name
        self.__record = record

    def __log_access(self, user):
        print(f"Record accessed by: {user}")

    def authenticate(self, user, password):
        return password == "admin123"

    def view_record(self, user, password):
        if self.authenticate(user, password):
            self.__log_access(user)
            return self.__record
        else:
            print("Authentication failed.")
            return None


# Example
p = HospitalPatient("Vikas", {"BP": "120/80", "Allergy": "None"})
print(p.view_record("DoctorA", "admin123"))
