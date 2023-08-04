# Yêu cầu:
# 1. nhập một chuỗi 
# có định dạng dd/MM/yyyy
# (ĐÂY LÀ NGÀY TRÊN TEM ĐĂNG KIỂM)

# 2. nhập một chuỗi 
# có định dạng dd/MM/yyyy
# (ĐÂY LÀ NGÀY HÔM NAY)

# 3. in ra kết quả phép trừ (dt1 - dt2)

# chương trình chính
import datetime

str1 = input()
str2 = input()

# tạo danh sách
ds1 = str1.split("/")
ds2 = str2.split("/")

# tạo đối tượng
dt1 = datetime.date(int(ds1[2]), int(ds1[1]), int(ds1[0]))
dt2 = datetime.date(int(ds2[2]), int(ds2[1]), int(ds2[0]))

ngay = (dt1 - dt2).days

print(ngay)