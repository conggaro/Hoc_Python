# Yêu cầu:
# 1. nhập số thực x
# 2. tính f1
# 3. tính f2

import math

x = float(input())

# tạo f1
f1 = 0

# tạo f2
f2 = 0

if x > 0:
    f1 = 3*x + x**0.5
    print(f"{f1:{'.'}3f}")

elif x <= 0:
    f1 = math.e**x + 4
    print(f"{f1:{'.'}3f}")

if x >= 1:
    f2 = math.sqrt(x**2 + 1)
    print(f"{f2:{'.'}3f}")

elif -1 < x and x < 1:
    f2 = 3*x + 5
    print(f"{f2:{'.'}3f}")

elif x <= -1:
    f2 = x**2 + 2*x - 1
    print(f"{f2:{'.'}3f}")