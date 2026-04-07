#Generator comprehensions
daily_sales = [
    4,67,34,23,67,89,45,23,56,78,90,12
]

sum_sales = (sale for sale in daily_sales if sale > 50)
print(sum(sum_sales))


# the generator compreghension helps us to write memory efficient code by generating values on the fly instead of storing them all in memory at once. In this example, the generator expression (sale for sale in daily_sales if sale > 50) creates an iterator that yields only the sales that are greater than 50. When we call sum(sum_sales), it iterates through the generator and sums up the values without needing to create a separate list to hold all the filtered sales. This can be particularly beneficial when dealing with large datasets, as it reduces memory usage and can improve performance.
