# Yêu cầu:
# 1. nhập chuỗi s
# 2. in ra "Yes" hoặc "No"

# |CHƯƠNG TRÌNH CHÍNH|
s = input()

dao_nguoc = ""

for i in range(len(s) - 1, -1, -1):
    dao_nguoc = dao_nguoc + s[i]

if s == dao_nguoc:
    print(f"Yes")

else:
    print(f"No")