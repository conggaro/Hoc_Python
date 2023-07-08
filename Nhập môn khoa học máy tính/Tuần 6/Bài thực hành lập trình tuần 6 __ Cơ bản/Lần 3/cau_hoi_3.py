# Yêu cầu:
# 1. nhập số thực x
# 2. nhập số nguyên n
# 3. in ra tổng S

# lấy 3 chữ số sau dấu phẩy thập phân

# chương trình chính
x = float(input())
n = int(input())

# hàm tính tổng S
def Tinh_S():
    global x, n

    S = 0

    for i in range(1, n + 1, 1):
        S = S + x**i

    print(f"{S:{'.'}3f}")

Tinh_S()