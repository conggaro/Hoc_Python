# Yêu cầu:
# 1. nhập n
# 2. nhập chuỗi string
# 3. in ra dãy tổng

# |CHƯƠNG TRÌNH CHÍNH|
n = int(input())

ds = []

for i in range(0, n, 1):
    diem_3_mon = input()

    item = diem_3_mon.split(" ")

    ds.append(item)

for i in range(0, n, 1):
    tong = 0

    for item in ds[i]:
        tong = tong + int(item)
    
    print(tong, end=" ")