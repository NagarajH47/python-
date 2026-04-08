text = input("Enter a string: ")

for ch in text:
    if ch.lower() in 'aeiou':
        continue
    print(ch, end="")