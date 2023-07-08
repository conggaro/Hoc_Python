# Yêu cầu:
# 1. nhập n
# 2. vẽ hình

n = int(input())

item = "*"

for i in range(0, n, 1):
    print(f" {item:{' '}^{n * 2}}")
    item = item + "**"

# xuống dòng
print()

item2 = "*****"
for i in range(0, n, 1):
    print(item2)

# xuống dòng
print()

item3 = "*"

for i in range(0, n, 1):
    print(f"{item3:{' '}<{n * 2}}")
    item3 = item3 + "**"

do_dai = len(item3) - 2

for i in range(0, n - 1, 1):
    do_dai = do_dai - 2
    print(f"{item3[0: do_dai: 1]:{' '}<{n * 2}}")