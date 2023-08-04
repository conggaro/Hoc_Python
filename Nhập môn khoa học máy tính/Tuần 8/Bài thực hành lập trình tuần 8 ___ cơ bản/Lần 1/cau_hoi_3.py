# Yêu cầu:
# 1. nhập họ tên
# 2. in ra họ

# chương trình chính
ho_ten = input()

ho_ten = ho_ten.lstrip()

vi_tri = ho_ten.find(" ", 0, len(ho_ten))

print(f"{ho_ten[0: vi_tri: 1]}")