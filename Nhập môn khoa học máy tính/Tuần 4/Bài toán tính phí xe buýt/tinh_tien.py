# Yêu cầu:
# 1. nhập giá tiền vé tháng
# 2. nhập họ tên
# 3. nhập tuổi
# 4. nhập số tháng muốn mua

# 5. in ra tổng số tiền khách phải trả
# khách hàng <= 18 tuổi thì được giảm giá 10%

tien_ve_thang = int(input("Nhap vao gia tien ve thang: "))

hoTen = input("Nhap vao ho va ten: ")

tuoi = int(input("Nhap vao tuoi: "))

so_thang = int(input("Nhap vao so thang: "))

giam_gia = 0

if tuoi <= 18:
    print("Ban duoc giam gia.")
    giam_gia = 10/100 # chỗ này là kiểu float

# bây giờ thì tính tiền cho khách
tong_tien = tien_ve_thang * so_thang - (tien_ve_thang*so_thang)*giam_gia

print(f"So tien khach phai tra la: {tong_tien:{'.'}0f} VND")