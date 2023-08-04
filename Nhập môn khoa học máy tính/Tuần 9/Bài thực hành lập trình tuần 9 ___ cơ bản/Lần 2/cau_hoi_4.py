# Yêu cầu:
# 1. nhập n
# 2. nhập n phần tử (kiểu float)
# 3. in ra tiền phải trả

# |CHƯƠNG TRÌNH CHÍNH|
n = int(input())

ds = []

for i in range(0, n, 1):
    item = float(input())

    ds.append(item)

tong = 0

for item in ds:
    if 7 <= item < 8:
        tong = tong + 1200000

    elif 8 <= item < 9:
        tong = tong + 1400000

    elif 9 <= item <= 10:
        tong = tong + 1800000

print(tong)