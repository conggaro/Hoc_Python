# Yêu cầu:
# 1. nhập số thực x
# 2. in ra f(x)
# 3. in ra g(x)

# lấy 2 chữ số sau dấu phẩy

# chương trình chính
x = float(input())

# hàm tính f(x)
def Tinh_f():
    global x
    f = 0

    if -1 <= x and x <= 1:
        f = (-2) * (x - 3)

    elif x > 1:
        f = (x**2 - 1)**(1/2)

    print(f"{f:{'.'}2f}")

# hàm tính g(x)
def Tinh_g():
    global x
    g = 0

    if x > 2:
        g = x**2 + 1

    elif -2 <= x and x <= 2:
        g = 2*x - 1

    elif x < -2:
        g = 6 - 5*x

    print(f"{g:{'.'}2f}")

Tinh_f()
Tinh_g()