# Yêu cầu:
# 1. nhập ngày trên tem đăng kiểm
# 2. nhập ngày hôm nay
# 3. in ra "CHUA HET HAN", "HOM NAY HET HAN", "DA HET HAN"

# dữ liệu nhập vào có định dạng dd/MM/yyyy

# |CHƯƠNG TRÌNH CHÍNH|
import datetime

str1 = input()
str2 = input()

# chuyển chuỗi string thành danh sách
ds1 = str1.split("/")
ds2 = str2.split("/")

# tạo đối tượng (datetime)
dt1 = datetime.date(int(ds1[2]), int(ds1[1]), int(ds1[0]))
dt2 = datetime.date(int(ds2[2]), int(ds2[1]), int(ds2[0]))

# tạo biến hạn đăng kiểm
han_dang_kiem = (dt1 - dt2).days

if han_dang_kiem > 0:
    print(f"CHUA HET HAN")

elif han_dang_kiem == 0:
    print(f"HOM NAY HET HAN")

elif han_dang_kiem < 0:
    print(f"DA HET HAN")