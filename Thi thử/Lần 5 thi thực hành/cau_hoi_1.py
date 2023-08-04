# Yêu cầu:
# 1. nhập x1
# 2. nhập y1
# 3. nhập z1
# 4. nhập ban_kinh1

# 5. nhập x2
# 6. nhập y2
# 7. nhập z2
# 8. nhập ban_kinh2

# OUTTER: Nếu hai hình cầu nằm ngoài nhau
# TOUCH: Nếu hai hình cầu tiếp xúc nhau.
# INNER: Nếu có một hình cầu nằm trong hình còn lại
# INTERSECT: Nếu hai hình cầu giao nhau

# |CHƯƠNG TRÌNH CHÍNH|
from math import sqrt
from math import pow

x1 = float(input())
y1 = float(input())
z1 = float(input())
r1 = float(input())

x2 = float(input())
y2 = float(input())
z2 = float(input())
r2 = float(input())

# gọi A là tâm của hình cầu thứ nhất
# gọi B là tâm của hình cầu thứ hai
# AB là khoảng cách giữa hai tâm

data1 = pow(x2 - x1, 2)
data2 = pow(y2 - y1, 2)
data3 = pow(z2 - z1, 2)

AB = sqrt(data1 + data2 + data3)

if r1 + r2 < AB:
    # ngoài nhau
    print(f"OUTTER")

elif r1 + r2 == AB:
    # giao nhau tại 1 điểm
    # còn gọi là tiếp xúc
    # đây là loại tiếp xúc ngoài
    print(f"TOUCH")

elif r1 == r2 and AB == 0:
    # trùng nhau
    # giao nhau tại mọi điểm
    print(f"INTERSECT")

elif min(r1, r2) + AB == max(r1, r2):
    # đây là loại tiếp xúc trong
    print(f"TOUCH")

elif min(r1, r2) + AB < max(r1, r2):
    # đây là loại trong nhau
    print(f"INNER")

else:
    # các trường hợp còn lại
    # là giao nhau
    print(f"INTERSECT")