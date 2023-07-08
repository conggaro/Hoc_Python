# Yêu cầu:
# 1. nhập a
# 2. nhập b
# 3. nhập c
# 4. giải phương trình bậc 2

import math

a = float(input("Nhap a: "))

while a == 0:
    a = float(input("Nhap lai a (a != 0): "))

b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

# tính delta
delta = b**2 - 4*a*c

if delta < 0:
    print(f"Phuong trinh vo nghiem!")

elif delta == 0:
    x = -b / (2*a)
    print(f"Phuong trinh co nghiem kep: x1 = x2 = {x:{'.'}2f}")

elif delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

    print(f"Phuong trinh co 2 nghiem: x1 = {x1:{'.'}2f}, x2 = {x2:{'.'}2f}")