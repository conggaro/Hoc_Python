# Yêu cầu:
# 1. nhập ngày đăng kiểm
# 2. nhập ngày hôm nay
# 3. in ra số hạn đăng kiểm còn lại của xe

# nhập dữ liệu theo định dạng dd/MM/yyyy

# |CHƯƠNG TRÌNH CHÍNH|
import datetime

str1 = input()
str2 = input()

# chuyển chuỗi string sang danh sách
ds1 = str1.split("/")
ds2 = str2.split("/")

# tạo đối tượng (datetime)
dt1 = datetime.date(int(ds1[2]), int(ds1[1]), int(ds1[0]))
dt2 = datetime.date(int(ds2[2]), int(ds2[1]), int(ds2[0]))

# tạo biến hạn đăng kiểm
han_dang_kiem = (dt1 - dt2).days

print(han_dang_kiem)