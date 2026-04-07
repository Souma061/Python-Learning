book_prices_inr = {
    "The Great Gatsby": 499,
    "To Kill a Mockingbird": 399,
    "1984": 299,
    "Pride and Prejudice": 349,
    "The Catcher in the Rye": 449,
    # "Pride and Prejudice": 349,
}


book_prices_usd = {book:round(price / 90, 2) for book,price in book_prices_inr.items() if price > 0}
print(book_prices_usd)
