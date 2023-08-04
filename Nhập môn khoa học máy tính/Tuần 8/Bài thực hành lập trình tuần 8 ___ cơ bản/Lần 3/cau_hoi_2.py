# Yêu cầu:
# 1. nhập chuỗi a
# 2. nhập chuỗi b
# 3. in ra số lần xuất hiện của b trong a

# |CHƯƠNG TRÌNH CHÍNH|
a = input()
b = input()

# lấy độ dài của b
do_dai = len(b)

tong = 0

for i in range(0, len(a), 1):
    dem = a[i: i + do_dai: 1].count(b)

    tong = tong + dem

print(tong)