# Yêu cầu:
# 1. nhập số thực x
# 2. nhập số nguyên n
# 3. in ra S

# lấy 3 chữ số sau dấu phẩy

import math

# chương trình chính
x = float(input())
n = int(input())

# hàm tính S
def Tinh_S():
    global x, n

    S = 0
    for i in range(1, n + 1, 1):
        S = S + math.pow(x, i)

    print(f"{S:{'.'}3f}")

Tinh_S()