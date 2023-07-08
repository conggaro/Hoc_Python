# Yêu cầu:
# 1. nhập tọa độ x1 góc trên bên trái
# 2. nhập tọa độ y1 góc trên bên trái
# 3. nhập chiều dài 1
# 4. nhập chiều rộng 1

# 5. nhập tọa độ x2 góc trên bên trái
# 6. nhập tọa độ y2 góc trên bên trái
# 7. nhập chiều dài 2
# 8. nhập chiều rộng 2

x1 = float(input())
y1 = float(input())
w1 = float(input())
h1 = float(input())

x2 = float(input())
y2 = float(input())
w2 = float(input())
h2 = float(input())

if x1 + w1 < x2 or x2 + w2 < x1 or y1 + h1 < y2 or y2 + h2 < y1:
    print(f"KHONGGIAONHAU")
else:
    print(f"GIAONHAU")