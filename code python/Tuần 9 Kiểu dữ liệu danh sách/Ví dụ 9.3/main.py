# Yêu cầu:
# 1. nhập n (n nằm trong đoạn [5, 15])
# 2. tạo ma trận 2 chiều (các giá trị được tạo tự động)
# 3. tính tổng các phần tử của ma trận trên đường chéo chính

# |CHƯƠNG TRÌNH CHÍNH|
import random

n = int(input("Nhap n: "))

while n < 5 or n > 15:
    n = int(input("Nhap lai n (n nằm trong đoạn [5, 15]): "))

# tạo danh sách
ds = []

for i in range(0, n, 1):
    item = []

    for j in range(0, n, 1):
        # viết code như này
        # thì nó sẽ rand trong khoảng -100 đến 99
        data = random.randrange(-100, 100)
        item.append(data)

    ds.append(item)

print()

# in ra màn hình
for i in range(0, n, 1):
    for j in range(0, n, 1):
        print(f"{ds[i][j]:<8}", end="")
    
    print(end="\n\n")

tong1 = 0
for i in range(0, n, 1):
    for j in range(i, n, 1):
        if i == j:
            tong1 = tong1 + ds[i][j]
            break

print(f"Tong cac phan tu tren duong cheo chinh: {tong1}")

tong2 = 0
ds.reverse()
for i in range(0, n, 1):
    for j in range(i, n, 1):
        if i == j:
            tong2 = tong2 + ds[i][j]
            break

print(f"Tong cac phan tu tren duong cheo phu: {tong2}")