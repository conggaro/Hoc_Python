# Yêu cầu:
# 1. nhập vào a
# 2. nhập vào b
# 3. nhập vào c
# 4. tìm nghiệm của phương trình bậc 2

# phương trình bậc 2 là cái loại
# ax^2 + bx + c = 0

# kết quả chỉ lấy 3 chữ số sau dấu phẩy

a = float(input())

b = float(input())

c = float(input())

delta = b**2 - 4*a*c

if a == 0:
    if b == 0:
        print("Phuong trinh vo nghiem!")
    
    elif b != 0:
        x = -c / b
        print(f"Phuong trinh co mot nghiem: x = {x:{'.'}3f}")

elif a != 0:
    if delta > 0:
        x1 = (-b + delta**(1/2)) / (2*a)
        x2 = (-b - delta**(1/2)) / (2*a)
        print(f"Phuong trinh co 2 nghiem: x1 = {x1:{'.'}3f} va x2 = {x2:{'.'}3f}")

    elif delta == 0:
        x = -b / (2*a)
        print(f"Phuong trinh co nghiem kep: x1 = x2 = {x:{'.'}3f}")

    elif delta < 0:
        print("Phuong trinh vo nghiem!")