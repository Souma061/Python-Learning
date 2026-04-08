def serve_chai():
    yield "cup 1: Chai"
    yield "cup 2: Masala Chai"
    yield "cup 3: Ginger Chai"


stall = serve_chai()


for cup in stall:
    print(cup)


def get_book_list():
    return [
        "The Great Gatsby",
        "To Kill a Mockingbird",
        "1984",
        "Pride and Prejudice",
        "The Catcher in the Rye"
        ]


def get_book_list_generator():
    yield "The Great Gatsby"
    yield "To Kill a Mockingbird"
    yield "1984"
    yield "Pride and Prejudice"
    yield "The Catcher in the Rye"

book = get_book_list_generator()
for b in book:
    print(b)

#or

print(next(book))
print(next(book))
print(next(book))
print(next(book))
print(next(book))


#   File "/home/soumabrata/Workspace/Learning/Python/Generators_Decorators/ch_1.py", line 37, in <module>
#     print(next(book))
#           ~~~~^^^^^^
# StopIteration


#This output occurs because the generator has been exhausted after yielding all the book titles. When we call next(book) after all the items have been yielded, it raises a StopIteration exception to indicate that there are no more items to yield from the generator. This is a normal behavior of generators in Python, and it signals that we have reached the end of the sequence.
