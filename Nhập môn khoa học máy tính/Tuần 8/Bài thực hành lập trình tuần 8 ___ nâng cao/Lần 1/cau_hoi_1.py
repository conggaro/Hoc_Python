# Yêu cầu:
# 1. nhập chuỗi
# có định dạng yyyy-MM-dd

# 2. in ra chuỗi
# có định dạng dd-MM-yyyy

# chương trình chính
str1 = input()

danh_sach = str1.split("-")

thoi_gian = []

for i in range(len(danh_sach) - 1, -1, -1):
    thoi_gian.append(danh_sach[i])

print("-".join(thoi_gian))