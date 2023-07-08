# cách 2:
# sử dụng hàm

import math

# hàm nhập dữ liệu
def Ham_NhapDuLieu():
    a = float(input("Nhap a: "))

    while a == 0:
        a = float(input("Nhap lai a (a != 0): "))

    b = float(input("Nhap b: "))
    c = float(input("Nhap c: "))

    return a, b, c

# hàm tính delta:
def Ham_Tinh_delta(a, b, c):
    delta = b**2 - 4*a*c

    return delta

# hàm phương trình vô nghiệm
def Ham_PhuongTrinhVoNghiem():
    print(f"Phuong trinh vo nghiem!")

# hàm phương trình có nghiệm kép
def Ham_PhuongTrinhCo_NghiemKep(a, b):
    x = -b / (2*a)
    print(f"Phuong trinh co nghiem kep: ", end="")
    print(f"x1 = x2 = {x:{'.'}2f}")

# hàm phương trình có 2 nghiệm
def Ham_PhuongTrinhCo_2_Nghiem(a, b, delta):
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

    print(f"Phuong trinh co 2 nghiem: ", end="")
    print(f"x1 = {x1:{'.'}2f}, x2 = {x2:{'.'}2f}")

# chương trình trính

# gọi hàm nhập dữ liệu
a, b, c = Ham_NhapDuLieu()

# gọi hàm tính delta
delta = Ham_Tinh_delta(a, b, c)

if delta < 0:
    # gọi hàm cho trường hợp vô nghiệm
    Ham_PhuongTrinhVoNghiem();

elif delta == 0:
    # gọi hàm cho trường hợp nghiệm kép
    Ham_PhuongTrinhCo_NghiemKep(a, b)

elif delta > 0:
    # gọi hàm cho trường hợp 2 nghiệm
    Ham_PhuongTrinhCo_2_Nghiem(a, b, delta)