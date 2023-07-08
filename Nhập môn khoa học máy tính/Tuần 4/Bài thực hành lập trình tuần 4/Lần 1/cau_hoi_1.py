# Yêu cầu:
# 1. nhập vào a
# 2. nhập vào b
# 3. nhập vào c
# 4. in ra kết quả sau khi giải phương trình bậc 2

# ax^2 + bx + c = 0

import math

a = float(input())

b = float(input())

c = float(input())

delta = math.pow(b, 2) - 4 * a * c

if a == 0:
    if b == 0:
        print(f"Phuong trinh vo nghiem!")
    
    elif b != 0:
        x = (-c) / b
        print(f"Phuong trinh co mot nghiem: x = {x:{'.'}3f}")

elif a != 0:
    if delta == 0:
        x = (-b) / (2*a)
        print(f"Phuong trinh co nghiem kep: x1 = x2 = {x:{'.'}3f}")

    elif delta > 0:
        x1 = ((-b) + math.sqrt(delta)) / (2*a)
        x2 = ((-b) - math.sqrt(delta)) / (2*a)
        print(f"Phuong trinh co 2 nghiem: x1 = {x1:{'.'}3f} va x2 = {x2:{'.'}3f}")

    elif delta < 0:
        print(f"Phuong trinh vo nghiem!")