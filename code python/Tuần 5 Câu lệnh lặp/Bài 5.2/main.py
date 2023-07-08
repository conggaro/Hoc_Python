# Yêu cầu:
# 1. nhập n
# 2. tính s

n = int(input("Nhap n: "))

s = 0

for i in range(1, n + 1, 1):
    s = s + 1/i

print(f"s = {s}")