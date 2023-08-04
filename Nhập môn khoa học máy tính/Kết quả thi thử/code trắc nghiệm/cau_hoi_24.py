ds1 = ["red", "big", "tasty"]

ds2 = ["apple", "banana", "cherry"]

for x in ds1:
    for y in ds2:
        if y == "banana":
            continue

        print(x, y)