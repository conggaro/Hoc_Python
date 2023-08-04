# Yêu cầu:
# 1. nhập chuỗi có định dạng yyyy-MM-dd
# 2. chuyển chuỗi đó thành định dạng dd-MM-yyyy

# |CHƯƠNG TRÌNH CHÍNH|
s = input()

# chuyển chuỗi sang danh sách
danh_sach = s.split("-")

# tạo biến khởi tạo
khoi_tao = []

for i in range(len(danh_sach) - 1, -1, -1):
    khoi_tao.append(danh_sach[i])

print("-".join(khoi_tao))