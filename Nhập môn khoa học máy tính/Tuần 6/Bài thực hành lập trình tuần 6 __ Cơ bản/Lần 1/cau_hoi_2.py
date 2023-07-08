# Yêu cầu:
# 1. nhập x
# 2. nhập y
# 3. nhập z
# 4. tính giá trị hàm số f(x, y)
# 5. tính giá trị hàm số f(x, y, z)

# hàm tính f(x, y)
def Tinh_HamSo_f1(x, y):
    ketQua = 0

    ketQua = x**2 + x*y + y**2 - 2*x - y

    print(f"{ketQua:{'.'}2f}")

# hàm tính f(x, y, z):
def Tinh_HamSo_f2(x, y, z):
    if y == 0:
        ketQua1 = "N/A"
        print(f"{ketQua1}")

    elif y != 0:
        ketQua2 = (x * y * z) + (x / y**z)
        print(f"{ketQua2:{'.'}2f}")

# chương trình chính
x = float(input())
y = float(input())
z = float(input())

Tinh_HamSo_f1(x, y)
Tinh_HamSo_f2(x, y, z)