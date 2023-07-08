# Yêu cầu:
# 1. nhập x
# 2. in ra f(x)
# 3. in ra g(x)

# hàm tính f(x)
def Tinh_HamSo_f(x):
    ketQua = 0

    if -1 <= x and x <= 1:
        ketQua = -2 * (x - 3)
    
    elif x > 1:
        ketQua = (x**2 - 1)**(1/2)

    return ketQua

# hàm tính g(x)
def Tinh_HamSo_g(x):
    ketQua = 0

    if x > 2:
        ketQua = x**2 + 1
    
    elif -2 <= x and x <= 2:
        ketQua = 2 * x - 1

    elif x < -2:
        ketQua = 6 - 5 * x

    return ketQua

# chương trình chính

x = float(input())

print(f"{Tinh_HamSo_f(x):{'.'}2f}")
print(f"{Tinh_HamSo_g(x):{'.'}2f}")