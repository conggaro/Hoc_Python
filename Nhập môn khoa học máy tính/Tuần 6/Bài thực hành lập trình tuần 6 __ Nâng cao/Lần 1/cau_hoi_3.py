# Yêu cầu
# 1. nhập x (số thực)
# 2. nhập m (số nguyên)
# 3. in ra Sin(x)

import math

# hàm tìm Sin(x)
def Tim_Sin(x, m):
    ketQua = 0

    # i sẽ chạy từ 0 đến (m-1)
    for i in range(1, m + 1, 1):
        ketQua = ketQua + ((-1)**(i - 1) * x**(2*i - 1)) / (math.factorial(2*i - 1))

    return ketQua

# chương trình chính
x = float(input())
m = int(input())

print(f"{Tim_Sin(x, m):{'.'}3f}")