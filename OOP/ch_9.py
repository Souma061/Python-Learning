#


class Validator:
    @staticmethod
    def isValidEmail(email):
        return "@" in email and "." in email

    @staticmethod
    def isValidPassword(password):
        return len(password) >= 8

    @staticmethod
    def isValidUsername(username):
        return len(username) >= 3




# Example usage
email = "user@example.com"
password = "securepassword"
username = "john_doe"

print(Validator.isValidEmail(email))  # True
print(Validator.isValidPassword(password))  # True
print(Validator.isValidUsername(username))  # True


#@static method is a decorator in Python that indicates that a method belongs to the class rather than an instance of the class. It can be called on the class itself without needing to create an instance. Static methods do not have access to the instance (self) or class (cls) variables and are typically used for utility functions that perform a specific task related to the class but do not require access to instance or class data.
