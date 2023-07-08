# Yêu cầu:
# 1. nhập vào tiền vé tháng
# 2. nhập vào tên
# 3. nhập vào tuổi
# 4. nhập vào số tháng muốn mua

# 5. tính tiền

# trường hợp 1: nhỏ hơn hoặc bằng 18 tuổi
# được giảm giá 10%

# trường hợp 2: lớn hơn hoặc bằng 60 tuổi
# miễn toàn bộ

# trường hợp 3: 18 < tuổi < 60
# không được miễn

giaVe = int(input("Nhap vao gia ve thang: "))

ten = input("Nhap vao ten: ")

tuoi = int(input("Nhap vao tuoi: "))

soThangMuonMua = int(input("Nhap vao so thang muon mua: "))

tongTien = 0

if 0 < tuoi and tuoi <= 18:
    print(f"Duoc giam gia 10%.")
    tongTien = giaVe * soThangMuonMua * (1 - 10/100)
    print(f"So tien phai tra la: {tongTien:{'.'}0f} VND.")

elif tuoi >= 60:
    print(f"Duoc mien toan bo.")
    print(f"So tien phai tra la: {tongTien:{'.'}0f} VND.")

elif tuoi > 18 and tuoi < 60:
    print(f"Khong duoc giam gia.")
    tongTien = giaVe * soThangMuonMua
    print(f"So tien phai tra la: {tongTien:{'.'}0f} VND.")