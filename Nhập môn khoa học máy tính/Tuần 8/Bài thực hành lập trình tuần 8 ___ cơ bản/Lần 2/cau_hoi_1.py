# Yêu cầu:
# 1. nhập họ tên
# 2. in ra tên

# chương trình chính
ho_ten = input()

ho_ten = ho_ten.rstrip();

vi_tri = ho_ten.rfind(" ", 0, len(ho_ten))

print(f"{ho_ten[vi_tri + 1: len(ho_ten): 1]}")