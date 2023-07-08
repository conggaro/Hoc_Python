# Yêu cầu:
# 1. nhập x
# 2. nhập y
# 3. nhập z
# 4. in ra f1(x, y)
# 5. in ra f2(x, y, z)

# lấy 2 chữ số sau dấu phẩy

# chương trình chính
x = float(input())
y = float(input())
z = float(input())

# hàm tính f1(x, y)
def Tinh_f1():
    global x
    global y

    f1 = x**2 + x*y + y**2 + - 2*x - y
    print(f"{f1:{'.'}2f}")

def Tinh_f2():
    global x, y, z

    if y == 0:
        print(f"N/A")

    else:
        f2 = x*y*z + x / (y**z)
        print(f"{f2:{'.'}2f}")

Tinh_f1()
Tinh_f2()
