# Q13. Unique Number Counter

numbers = []

for i in range(10):
    n = int(input("Enter number: "))
    numbers.append(n)

unique_numbers = set(numbers)

print("Unique Numbers Count:", len(unique_numbers))