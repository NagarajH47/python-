# Q21. HackerRank Style Problem

numbers = [10, 20, 30, 40, 50]

# Find Maximum
maximum = numbers[0]

for n in numbers:
    if n > maximum:
        maximum = n

# Find Minimum
minimum = numbers[0]

for n in numbers:
    if n < minimum:
        minimum = n

# Reverse List
reversed_list = []

for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])

print("Maximum:", maximum)
print("Minimum:", minimum)
print("Reversed List:", reversed_list)