# Yêu cầu:
# 1. nhập chuỗi s
# 2. đếm từ
# 3. in ra biến đếm

# chương trình chính
s = input()

dem = 0

if s[0] != " ":
        dem += 1

for i in range(0, len(s) - 1, 1):
    if s[i] == " " and s[i + 1] != " ":
        dem += 1

print(f"{dem}")