# Logger with decorators

from functools import wraps
def logging(func):
    wraps(func)
    def wrapper(*args,**keywords):
      print(f"Function {func.__name__} is called with arguments {args} ")
      result = func(*args,**keywords)
      print(f"Function {func.__name__} returned {result}")
      return result

    return wrapper


@logging
def add(x,y):
    return x+y


add(5,3)
