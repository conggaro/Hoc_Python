# Yêu cầu:
# 1. nhập số thực x
# 2. nhập số nguyên n
# 3. in ra kết quả

# lấy 3 chữ số sau dấu phẩy

# |CHƯƠNG TRÌNH CHÍNH|
from math import factorial

x = float(input())

n = int(input())

tong = 1

for i in range(1, n + 1, 1):
    mau = factorial(i)
    tong = tong + (pow(x, i) / mau)

print(f"{tong:{'.'}3f}")