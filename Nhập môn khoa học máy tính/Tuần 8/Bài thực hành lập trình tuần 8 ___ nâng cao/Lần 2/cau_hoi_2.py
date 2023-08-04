# Yêu cầu:
# 1. nhập vào một chuỗi
# 2. chuyển định dạng Mỹ sang định dạng Việ Nam

# |CHƯƠNG TRÌNH CHÍNH|
s = input()

# hàm replace
# thì trả về 1 bản sao của chuỗi s
s = s.replace(",", ".")                 # thay thế dấu "," thành dấu "."

# tìm vị trí của dấu chấm đầu tiên
# từ phải sang trái
vi_tri = 0

for i in range(len(s) - 1, -1, -1):
    if s[i] == ".":
        vi_tri = i
        break

if vi_tri > 0:
    str1 = s[0: vi_tri: 1]

    # nếu gặp dấu chấm
    # thì thay thế bằng dấu phẩy
    # nếu không gặp dấu "." thì bỏ qua thôi
    str2 = s[vi_tri: len(s): 1].replace(".", ",")

s = str1 + str2

print(s)