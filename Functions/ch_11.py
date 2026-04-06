#types of functions: pure functions, impure functions, recursive functions, higher order functions, anonymous functions (lambda functions), generator functions, and more.

# Pure functions: A pure function is a function that always produces the same output for the same input and has no side effects (it does not modify any external state). Example:

#impure function: A function that has side effects or relies on external state is called an impure function.

# Recursive functions: A recursive function is a function that calls itself in order to solve a problem. Example:

# Higher-order functions: A higher-order function is a function that takes one or more functions as arguments and/or returns a function as its result. Example:

# Anonymous functions (lambda functions): A lambda function is a small, anonymous function defined using the lambda keyword. Example:

# Generator functions: A generator function is a special type of function that returns an iterator and can be used to generate a sequence of values on-the-fly. Example:


def pure_function(x):
    return x * 2

total = 0

def impure_function(x):
    global total  #Not recommended to use global variables in practice
    total += x
    return total

def recursive_function(n):
    if n <= 0:
        return 1
    else:
        return n * recursive_function(n - 1)

      #dry run of recursive function
      # recursive_function(3)
      # 3 * recursive_function(2)
      # 3 * (2 * recursive_function(1))
      # 3 * (2 * (1 * recursive_function(0)))
      # 3 * (2 * (1 * 1))

fact = recursive_function(3)  # Output: 6
print(fact)



names = ["Alice", "Bob", "Charlie","Alice", "Bob"]

filter_names = list(filter(lambda name: name != "Alice", names))

print(filter_names)  # Output: ['Bob', 'Charlie', 'Bob']
print(filter_names) #if name == 0  then it will return false and it will not be included in the output list. If name is not equal to "Alice", it will return true and the name will be included in the output list.


