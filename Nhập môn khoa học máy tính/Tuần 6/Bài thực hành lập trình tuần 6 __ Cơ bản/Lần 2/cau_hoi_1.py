# Yêu cầu:
# 1. nhập x
# 2. in ra f(x)
# 3. in ra g(x)

# lấy 2 chữ số sau dấu phẩy

# hàm tính f(x)
def Tinh_f(thamSo):
    ketQua = 0

    if -1 <= thamSo and thamSo <= 1:
        ketQua = (-2) * (thamSo - 3)

    elif thamSo > 1:
        ketQua = (thamSo**2 - 1)**(1/2)

    return ketQua

# hàm tính g(x)
def Tinh_g(thamSo):
    ketQua = 0

    if thamSo > 2:
        ketQua = thamSo**2 + 1

    elif -2 <= thamSo and thamSo <= 2:
        ketQua = 2*thamSo - 1

    elif thamSo < -2:
        ketQua = 6 - 5*thamSo

    return ketQua

# chương trình chính
x = float(input())

f = Tinh_f(x)

g = Tinh_g(x)

print(f"{f:{'.'}2f}")
print(f"{g:{'.'}2f}")