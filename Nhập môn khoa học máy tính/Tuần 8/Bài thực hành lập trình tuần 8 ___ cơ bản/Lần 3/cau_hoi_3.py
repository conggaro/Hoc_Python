# Yêu cầu:
# 1. nhập chuỗi s
# 2. in ra số từ đếm được

# |CHƯƠNG TRÌNH CHÍNH|
s = input()

dem = 0

if s[0] != " ":
    dem += 1

# thuật toán này
# i == n - 2
# thì dừng
for i in range(0, len(s) - 1, 1):
    if s[i] == " " and s[i + 1] != " ":
        dem += 1

print(f"{dem}")