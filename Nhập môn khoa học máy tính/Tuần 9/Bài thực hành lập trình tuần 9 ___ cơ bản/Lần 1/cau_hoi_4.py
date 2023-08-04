# Yêu cầu:
# 1. nhập n
# 2. nhập n phần tử
# 3. in ra tổng số tiền

# |CHƯƠNG TRÌNH CHÍNH|
n = int(input())

ds = []

for i in range(0, n, 1):
    item = float(input())

    ds.append(item)

tong_tien = 0

for item in ds:
    if 7 <= item < 8:
        tong_tien = tong_tien + 1200000
    
    elif 8 <= item < 9:
        tong_tien = tong_tien + 1400000

    elif 9 <= item <= 10:
        tong_tien = tong_tien + 1800000

print(tong_tien)