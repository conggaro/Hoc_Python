ds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(0, len(ds), 1):
    print(ds[i], end=" ")

print(end="\n")

for i in range(-len(ds), 0, 1):
    print(ds[i], end=" ")

print(end="\n\n")

print(f"ds[{-len(ds)}] = {ds[-len(ds)]}")
print(f"ds[{-len(ds) + 1}] = {ds[-len(ds) + 1]}")

print(end="\n")

print(f"ds[-2] = {ds[-2]}")
print(f"ds[-1] = {ds[-1]}")