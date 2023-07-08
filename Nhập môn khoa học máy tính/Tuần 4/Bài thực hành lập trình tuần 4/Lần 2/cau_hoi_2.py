# Yêu cầu:
# 1. nhập tọa độ x1 (đường tròn thứ 1)
# 2. nhập tọa độ y1 (đường tròn thứ 1)
# 3. nhập bán kính r1 (đường tròn thứ 1)

# 4. nhập tọa độ x2 (đường tròn thứ 2)
# 5. nhập tọa độ y2 (đường tròn thứ 2)
# 6. nhập bán kính r2 (đường tròn thứ 2)

# 7. in ra vị trí của 2 đường tròn

# GIAO NHAU
# nếu 2 đường tròn giao nhau

# NGOÀI NHAU
# nếu 2 đường tròn nằm ngoài nhau

# TRONG NHAU
# nếu 1 đường tròn nằm trong đường tròn còn lại

# TIẾP XÚC
# nếu 2 đường tròn tiếp xúc nhau

import math

x1 = float(input())
y1 = float(input())
r1 = float(input())

x2 = float(input())
y2 = float(input())
r2 = float(input())

# gọi A là tâm của đường tròn thứ 1
# gọi B là tâm của đường tròn thứ 2
# gọi AB là khoảng cách từ tâm đường tròn thứ nhất đến tâm đường tròn thứ 2

AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if (r1 + r2 > AB):
    if (AB > r1 and AB > r2):
        print(f"GIAONHAU") # loại này thì giao nhau nhưng tâm nó ở ngoài
    
    elif (r1 - r2 == AB) or (r2 - r1 == AB):
        print(f"TIEPXUC") # đây là cái loại tiếp xúc trong

    elif (AB + r1/2 < r2) or (AB + r2/2 < r1):
        print(f"TRONGNHAU")

    elif (AB < r1 or AB < r2):
        print(f"GIAONHAU") # loại này thì giao nhau nhưng tâm nó ở trong

elif (r1 + r2 < AB):
    print(f"NGOAINHAU")
    
elif (r1 + r2 == AB):
    # cái trường hợp r1 + r2 == AB
    # thì gọi là tiếp xúc ngoài
    print(f"TIEPXUC")