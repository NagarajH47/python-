# Q20. Mini Banking System

balance = 1000

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
    else:
        print("Insufficient Balance")

def check_balance():
    print("Balance:", balance)

deposit(500)
withdraw(300)
check_balance()