# Yêu cầu:
# 1. nhập tên
# 2. nhập năm sinh
# 3. in ra màn hình người đó năm nay bao nhiêu tuổi

from datetime import date

ten = input("Nhap vao ten: ")

namSinh = int(input("Nhap vao nam sinh: "))

namHienTai = date.today().year

print(f"Ho va ten: {ten}")
print(f"Tuoi: {namHienTai - namSinh}")