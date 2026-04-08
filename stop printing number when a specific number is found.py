n = int(input("Enter the limit: "))
stop = int(input("Enter the number to stop at: "))

for i in range(1, n + 1):
    if i == stop:
        break
    print(i)