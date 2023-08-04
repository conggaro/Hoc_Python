num = 0

while num < 10:
    num += 2

    if num % 3 == 0:
        continue

    print(num, end=" ")