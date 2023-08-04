# Yêu cầu:
# 1. nhập một chuỗi 
# có định dạng dd/MM/yyyy
# (ĐÂY LÀ NGÀY TRÊN TEM ĐĂNG KIỂM)

# 2. nhập một chuỗi 
# có định dạng dd/MM/yyyy
# (ĐÂY LÀ NGÀY HÔM NAY)

# 3. tính kết quả phép trừ (dt1 - dt2)
# in ra "CHUA HET HAN"
# hoặc in ra "HOM NAY HET HAN"
# hoặc in ra "DA HET HAN"

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

if ngay > 0:
    print(f"CHUA HET HAN")

elif ngay == 0:
    print(f"HOM NAY HET HAN")

else:
    print(f"DA HET HAN")