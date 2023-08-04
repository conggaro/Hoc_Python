# Yêu cầu:
# 1. nhập x1, y1, z1, ban_kinh1
# 2. nhập x2, y2, z2, ban_kinh2

# 3. in ra kết quả tương ứng
# INTERSECT     --> nếu 2 hình cầu giao nhau
# OUTTER        --> nếu 2 hình cầu ngoài nhau
# INNER         --> nếu có 1 hình cầu nằm trong hình cầu còn lại
# TOUCH         --> hai hình cầu tiếp xúc nhau

# |CHƯƠNG TRÌNH CHÍNH|
from math import sqrt
from math import pow

x1 = float(input())
y1 = float(input())
z1 = float(input())
ban_kinh1 = float(input())

x2 = float(input())
y2 = float(input())
z2 = float(input())
ban_kinh2 = float(input())

# gọi tâm của hình cầu thứ nhất là A
# gọi tâm của hình cầu thứ hai là B
# AB là khoảng cách giữa 2 tâm

data1 = pow(x2 - x1, 2)
data2 = pow(y2 - y1, 2)
data3 = pow(z2 - z1, 2)

AB = sqrt(data1 + data2 + data3)

if ban_kinh1 + ban_kinh2 < AB:
    # ngoài nhau
    print(f"OUTTER")

elif ban_kinh1 + ban_kinh2 == AB:
    # tiếp xúc ngoài
    print(f"TOUCH")

elif ban_kinh1 == ban_kinh2 and AB == 0:
    # trùng nhau
    print(f"TOUCH")

elif min(ban_kinh1, ban_kinh2) + AB == max(ban_kinh1, ban_kinh2):
    # tiếp xúc trong
    print(f"TOUCH")

elif min(ban_kinh1, ban_kinh2) + AB < max(ban_kinh1, ban_kinh2):
    # trong nhau
    print(f"INNER")

else:
    # còn lại là giao nhau
    print(f"INTERSECT")