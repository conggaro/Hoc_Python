# Yêu cầu:
# 1. nhập n
# 2. vẽ hình

n = int(input())

item1 = "*"

for i in range(1, n + 1, 1):
    print(f" {item1:{' '}^{n * 2}}")
    item1 = item1 + "**"

# xuống dòng
print(end="\n")

item2 = "*****"
for i in range(0, n, 1):
    print(f"{item2}")

# xuống dòng
print(end="\n")

item3 = "*"

for i in range(1, n + 1, 1):
    print(f"{item3:{' '}<{n * 2}}")
    item3 = item3 + "**"

do_dai = (n * 2 + 1) - 2
for i in range(1, n, 1):
    do_dai = do_dai - 2
    print(f"{item3[0: do_dai: 1]:{' '}<{n * 2}}")