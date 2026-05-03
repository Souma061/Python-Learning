

# Write a one-liner to get only even numbers
# Expected output: [2, 4, 6, 8, 10]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_nums = [num for num in numbers if num % 2 == 0]

print(even_nums)


# Write a function that takes a list of salaries
# and returns how many are above average


# Expected output: 2  (80000 and 60000 are above average)

salaries = [25000, 45000, 30000, 80000, 60000, 15000]

def count_average_salaries(salaries):
    average_salary = sum(salaries) / len(salaries)
    return sum(1 for salary in salaries if salary > average_salary)


# result = count_average_salaries(salaries)
# print(result)


# Create a class called BankAccount with:
# - balance attribute starting at 0
# - deposit(amount) method
# - withdraw(amount) method (should not go below 0)
# - get_balance() method

# Should work like this:
# acc = BankAccount()
# acc.deposit(5000)
# acc.withdraw(2000)
# print(acc.get_balance())  # 3000
# acc.withdraw(9999)
# print(acc.get_balance())  # still 3000, can't go below 0



# acc = BankAccount()
# acc.deposit(5000)
# acc.withdraw(2000)
# print(acc.get_balance())  # 3000
# acc.withdraw(9999)
# print(acc.get_balance())  # still 3000, can't go below 0


class BankAccount:
    def __init__(self) -> None:
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount

    def Withdraw(self,amount):
        if self.balance - amount >= 0:
            self.balance -= amount

    def get_balance(self):
        if self.balance < 0:
            return 0
        return self.balance


acc = BankAccount()
acc.deposit(5000)
acc.Withdraw(2000)
print(acc.get_balance())
acc.Withdraw(9999)
print(acc.get_balance())
