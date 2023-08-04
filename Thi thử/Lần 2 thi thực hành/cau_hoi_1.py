# Yêu cầu:
# 1. nhập x1
# 2. nhập y1
# 3. nhập z1
# 4. nhập ban_kinh1

# 5. nhập x2
# 6. nhập y2
# 7. nhập z2
# 8. nhập ban_kinh2

# 9. in ra kết quả tương ứng
# OUTTER
# TOUCH
# INNER
# INTERSECT

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

# gọi A là tâm của hình cầu thứ nhất
# gọi B là tâm của hình cầu thứ hai
# AB là khoảng cách giữa 2 tâm

data1 = pow(x2 - x1, 2)
data2 = pow(y2 - y1, 2)
data3 = pow(z2 - z1, 2)

AB = sqrt(data1 + data2 + data3)

if ban_kinh1 + ban_kinh2 < AB:
    # ngoài nhau
    print(f"OUTTER")

elif ban_kinh1 + ban_kinh2 == AB:
    # tiếp xúc bên ngoài
    print(f"TOUCH")

elif ban_kinh1 == ban_kinh2 and AB == 0:
    # trùng nhau
    # tiếp xúc tại mọi điểm
    print(f"TOUCH")

elif min(ban_kinh1, ban_kinh2) + AB == max(ban_kinh1, ban_kinh2):
    # tiếp xúc trong
    print(f"TOUCH")

elif min(ban_kinh1, ban_kinh2) + AB < max(ban_kinh1, ban_kinh2):
    # trong nhau
    print(f"INNER")

else:
    # các trường hợp còn lại
    # là giao nhau
    print(f"INTERSECT")