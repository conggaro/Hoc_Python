# Yêu cầu:
# 1. nhập a
# 2. nhập b
# 3. nhập c

# 4. kiểm tra 3 cạnh đó có phải là 3 cạnh của 1 tam giác không

# 5. nếu là 3 cạnh của 1 tam giác thì tính diện tích tam giác đó

import math

a = float(input(f"Nhap vao a: "))

b = float(input(f"Nhap vao b: "))

c = float(input(f"Nhap vao c: "))


kiemTra1 = True if a > 0 else False # phép toán 3 ngôi
kiemTra2 = True if b > 0 else False
kiemTra3 = True if c > 0 else False

kiemTra4 = True if (a+b) > c else False
kiemTra5 = True if (b+c) > a else False
kiemTra6 = True if (a+c) > b else False

if kiemTra1 and kiemTra2 and kiemTra3 and kiemTra4 and kiemTra5 and kiemTra6:
    print(f"a, b, c la 3 canh cua 1 tam giac")
    tong = a + b + c
    p = tong / 2
    dienTich = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"Dien tich tam giac la: {dienTich:{'.'}6f}")

else:
    print(f"a, b, c khong phai 3 canh cua 1 tam giac")