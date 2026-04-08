from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper


@my_decorator
def greet():
    print("Hello, World!")


greet()
print(greet.__name__)  # Output: wrapper
# Output: Before the function call.
#         Hello, World!
#         After the function call.
#         greet
