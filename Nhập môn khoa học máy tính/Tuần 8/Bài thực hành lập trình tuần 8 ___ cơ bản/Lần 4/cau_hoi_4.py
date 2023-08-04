# Yêu cầu:
# 1. nhập họ tên
# 2. lấy ra tên

# |CHƯƠNG TRÌNH CHÍNH|
ho_ten = input()

# xóa hết khoảng trắng bên phải
ho_ten = ho_ten.rstrip()

# vị trí khoảng trống đầu tiên
# tìm từ phải sang trái
vi_tri = ho_ten.rfind(" ", 0, len(ho_ten))

print(ho_ten[vi_tri + 1: len(ho_ten): 1])