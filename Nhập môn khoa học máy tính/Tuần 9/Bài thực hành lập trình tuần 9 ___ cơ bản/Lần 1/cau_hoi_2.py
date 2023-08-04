# Yêu cầu:
# 1. nhập n
# 2. nhập điểm trúng tuyển
# 3. nhập n phần tử
# 4. in ra danh sách trúng tuyển

# |CHƯƠNG TRÌNH CHÍNH|
n = int(input())

diem_TrungTuyen = float(input())

ds = []

for i in range(0, n, 1):
    item = float(input())
    ds.append(item)

for i in range(0, n, 1):
    if ds[i] >= diem_TrungTuyen:
        print(f"{ds[i]}", end=" ")