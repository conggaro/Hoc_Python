# Yêu cầu:
# 1. nhập chuỗi s
# 2. in ra "Yes" hoặc "No"

# chương trình chính
s = input()

kiemTra = ""

for i in range(len(s) - 1, -1, -1):
    kiemTra = kiemTra + s[i]

if kiemTra == s:
    print(f"Yes")

else:
    print(f"No")