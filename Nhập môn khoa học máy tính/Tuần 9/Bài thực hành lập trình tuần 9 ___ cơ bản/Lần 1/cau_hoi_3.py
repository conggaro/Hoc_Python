# Yêu cầu:
# 1. nhập n

# 2. nhập n phần tử
# mỗi phần tử là một chuỗi string
# ví dụ: "6 7 8"

# 3. in ra danh sách tổng điểm của n phần tử

# |CHƯƠNG TRÌNH CHÍNH|
n = int(input())

ds = []

for i in range(0, n, 1):
    # nhập chuỗi string
    chuoi_string = input()
    
    item = chuoi_string.split(" ")

    ds.append(item)

for i in range(0, n, 1):
    tong = 0

    for j in range(0, len(ds[i]), 1):
        tong = tong + int(ds[i][j])

    print(f"{tong}", end=" ")