# Yêu cầu:
# 1. nhập họ tên
# 2. in ra họ

# |CHƯƠNG TRÌNH CHÍNH|
ho_ten = input()

# xóa khoảng trắng thừa bên trái
ho_ten = ho_ten.lstrip()

# tìm vị trí dấu cách đầu tiên
vi_tri = ho_ten.find(" ", 0, len(ho_ten))

print(ho_ten[0: vi_tri: 1])