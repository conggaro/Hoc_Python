# Yêu cầu:
# 1. nhập n
# 2. nhập n phần tử
# 3. in ra "SORTED" hoặc vị trí

# |CHƯƠNG TRÌNH CHÍNH|
n = int(input())

ds = []

for i in range(0, n, 1):
    item = int(input())

    ds.append(item)

ketQua = "SORTED"

for i in range(0, n - 1, 1):
    if ds[i] < ds[i + 1]:
        ketQua = f"{i + 1}"
        break

print(ketQua)