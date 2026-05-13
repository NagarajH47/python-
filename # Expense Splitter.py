# Expense Splitter

expenses = [1200, 850, 1500, 950]

total = sum(expenses)
average = total / len(expenses)

highest_paid = max(expenses)
person = expenses.index(highest_paid) + 1

print("Expenses:", expenses)
print("Total Expense:", total)
print("Average Share:", average)
print("Person", person, "paid highest:", highest_paid)

print("\nEqual Contribution Details:")

for i in range(len(expenses)):
    difference = expenses[i] - average

    if difference > 0:
        print("Person", i + 1, "should receive", difference)
    elif difference < 0:
        print("Person", i + 1, "should pay", abs(difference))
    else:
        print("Person", i + 1, "is settled")