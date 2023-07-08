# Yêu cầu:
# 1. nhập số thực x
# 2. nhập số nguyên m
# 3. in ra kết quả Sin(x)

# lấy 3 chữ số sau dấu phẩy thập phân

from math import pow

# hàm tính giai thừa
from math import factorial

# chương trình chính
x = float(input())
m = int(input())

# hàm tính Sin(x)
def Tinh_Sin():
    global x, m

    tong = 0

    for i in range(1, m + 1, 1):
        tong = tong + pow(-1, i - 1) * pow(x, 2*i - 1) / factorial(2*i - 1)

    print(f"{tong:{'.'}3f}")

Tinh_Sin()