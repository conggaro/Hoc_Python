# Yêu cầu:
# 1. nhập x
# 2. nhập n
# 3. in ra S(x, n)

# hàm tính S(x, n)
def Tinh_HamSo_S(x, n):
    ketQua = 0

    for i in range(1, n + 1, 1):
        ketQua = ketQua + x**i

    print(f"{ketQua:{'.'}3f}")

# chương trình chính
x = float(input())
n = int(input())

Tinh_HamSo_S(x, n)