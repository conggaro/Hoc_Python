# Yêu cầu:
# 1. nhập một chuỗi số n
# 2. chuyển định dạng Mỹ sang định dạng Việt Nam

# |CHƯƠNG TRÌNH CHÍNH|
n = input()

# nếu có dấu ","
# thay thế tất cả dấu phẩy thành dấu chấm
n = n.replace(",", ".")

# tìm vị trí của dấu chấm đầu tiên
# từ phải sang trái
vi_tri = n.rfind(".")

str1 = n[0: vi_tri: 1]
str2 = n[vi_tri: len(n): 1].replace(".", ",")

n = str1 + str2

print(n)