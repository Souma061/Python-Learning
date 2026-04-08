#infinite generators

#It is very useful when we want to generate an infinite sequence of values, such as the Fibonacci sequence, prime numbers, or even an infinite stream of random numbers. By using a generator, we can produce values on-the-fly without having to store the entire sequence in memory, which is especially beneficial when dealing with large or infinite data sets.


def infinite_numbers():
    count = 1
    while True:
        yield f"Refiel  {count}"
        count += 3


refil = infinite_numbers()
user2 = infinite_numbers()
for _ in range(10):
    print(next(refil))


for _ in range(10):
    print(next(user2))
