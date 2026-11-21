from bank import BankAccount

b = BankAccount(1000)

# Access balance
print("Balance:", b.balance)

# Update balance
b.balance = 5000
print("Updated balance:", b.balance)

# Try invalid balance
b.balance = -200
print("Final balance:", b.balance)