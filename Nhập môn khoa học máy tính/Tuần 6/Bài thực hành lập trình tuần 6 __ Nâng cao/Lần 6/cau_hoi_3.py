# Yêu cầu:
# 1. nhập số thực x
# 2. nhập số nguyên m
# 3. tính Sin(x)

# lấy 3 chữ số sau dấu phẩy thập phân

from math import pow
from math import factorial

# chương trình chính
x = float(input())
m = int(input())

# hàm tính Sin(x)
def Tinh_Sin():
    global x, m
    
    ketQua = 0

    for i in range(1, m + 1, 1):
        ketQua = ketQua + pow(-1, i - 1) * pow(x, 2*i - 1) / factorial(2*i - 1)

    print(f"{ketQua:{'.'}3f}")

Tinh_Sin()