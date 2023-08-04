# Yêu cầu:
# 1. nhập chuỗi s
# 2. in ra chuỗi đảo ngược

# chương trình chính
s = input()

dao_nguoc = ""

for i in range(len(s) - 1, -1, -1):
    dao_nguoc = dao_nguoc + s[i];

print(f"{dao_nguoc}")