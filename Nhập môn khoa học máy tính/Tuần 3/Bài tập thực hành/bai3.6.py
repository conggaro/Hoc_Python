# Yêu cầu:
# 1. nhập vào số giờ làm việc trong tuần

# 2. nhập vào số tiền phải trả 
# ví dụ 15k/giờ

# 3. in ra số tiền phải trả cho nhân viên

so_gio = int(input("Nhap vao so gio lam viec: ")) # số giờ làm việc

tien_lam_trong_1_gio = int(input("Nhap vao tien trong 1 gio: ")) # tiền/giờ

tien_phai_tra = so_gio * tien_lam_trong_1_gio # tiền phải trả

print(f"So tien phai tra cho nhan vien la: {tien_phai_tra} VND")

