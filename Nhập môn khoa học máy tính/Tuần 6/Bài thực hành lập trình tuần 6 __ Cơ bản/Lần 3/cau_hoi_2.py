# Yêu cầu:
# 1. nhập số thực x
# 2. nhập số thực y
# 3. nhập số thực z
# 4. in ra f1(x, y)
# 5. in ra f2(x, y, z)

# lấy 2 chữ số sau dấu phẩy

# chương trình chính
x = float(input())
y = float(input())
z = float(input())

# hàm tính f1
def Tinh_f1():
    global x, y

    f1 = x**2 + x*y + y**2 - 2*x - y

    print(f"{f1:{'.'}2f}")

# hàm tính f2
def Tinh_f2():
    global x, y, z

    f2 = 0

    if y == 0:
        print(f"N/A")

    elif y != 0:
        f2 = x*y*z + x / (y**z)
        print(f"{f2:{'.'}2f}")

Tinh_f1()
Tinh_f2()