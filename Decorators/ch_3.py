from functools import wraps

def require_admins(func):
    @wraps(func)
    def wrapper(user_roles):
        if user_roles != 'admin':
            print("Access denied. Admins only.")
            return None
        else:
            return func(user_roles)
    return wrapper

@require_admins
def access_sensitive_data(user_roles):
    print("Accessing sensitive data...")


access_sensitive_data('user')  # Output: Access denied. Admins only.
access_sensitive_data('admin')  # Output: Accessing sensitive data...
