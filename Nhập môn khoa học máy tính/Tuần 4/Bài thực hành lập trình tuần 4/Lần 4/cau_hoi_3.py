# Yêu cầu:
# 1. nhập giá trị thực x
# 2. tính f1
# 3. tính f2

import math

x = float(input())

f1 = 0

f2 = 0

if x > 0:
    f1 = 3*x + x**(1/2)

else:
    f1 = math.e**x + 4

if x >= 1:
    f2 = (x**2 + 1)**(1/2)

elif -1 < x and x < 1:
    f2 = 3*x + 5

elif x <= -1:
    f2 = x**2 + 2*x - 1

print(f"{f1:{'.'}3f}")
print(f"{f2:{'.'}3f}")