# Yêu cầu:
# 1. nhập x1
# 2. nhập y1
# 3. nhập r1

# 4. nhập x2
# 5. nhập y2
# 6. nhập r2

# 7. in ra nhận xét

x1 = float(input())
y1 = float(input())
r1 = float(input())

x2 = float(input())
y2 = float(input())
r2 = float(input())

# gọi A là tâm đường tròn 1
# gọi B là tâm đường tròn 2
# AB là khoảng cách giữa hai tâm đường tròn

AB = ((x2 - x1)**2 + (y2 - y1)**2)**float(1/2)

if r1 + r2 < AB:
    print(f"NGOAINHAU")

elif r1 + r2 == AB:
    print(f"TIEPXUC") # đây là cái loại tiếp xúc ngoài

elif r1 + r2 > AB:
    if r1 - r2 == AB or r2 - r1 == AB:
        print(f"TIEPXUC") # đây là cái loại tiếp xúc trong

    elif AB + r1 < r2 or AB + r2 < r1:
        print(f"TRONGNHAU")

    elif AB > r1 and AB > r2:
        print(f"GIAONHAU") # giao nhau nhưng tâm nó ở ngoài

    elif AB < r1 or AB < r2:
        print(f"GIAONHAU") # giao nhau nhưng tâm nó ở trong