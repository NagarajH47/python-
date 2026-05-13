# Pattern Compression

data = [1, 1, 1, 2, 2, 3, 3, 3]

result = []

count = 1

for i in range(len(data)):

    if i < len(data) - 1 and data[i] == data[i + 1]:
        count += 1
    else:
        result.append((data[i], count))
        count = 1

print("Input:", data)
print("Compressed Output:", result)