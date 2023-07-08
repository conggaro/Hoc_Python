# Yêu cầu:
# 1. nhập n
# 2. tính sa
# 3. tính sb

n = int(input())

sa = 0
sb = 1

for i in range(1, n + 1, 1):
    sa = sa + i**2

for i in range(1, n + 1, 1):
    sb = sb + 1/(i * (i + 1))

print(f"{sa:{'.'}3f}")
print(f"{sb:{'.'}3f}")