# Yêu cầu
# 1. nhập giá tiền vé tháng
# 2. nhập tên
# 3. nhập tuổi
# 4. nhập số tháng muốn mua

# 5. in ra màn hình được giảm giá nếu khách nhỏ hơn hoặc bằng 18 tuổi
# 6. in ra màn hình không được giảm giá nếu khách trên 18 tuổi

# 7. in ra số tiền khách phải trả

tienVeThang = int(input("Nhap gia tien ve thang: "))

ten = input("Nhap ten: ")

tuoi = int(input("Nhap tuoi: "))

soThangMuonMua = int(input("Nhap so thang muon mua: "))

giamGia = 0

if tuoi <= 18:
    print(f"Duoc giam gia.")
    giamGia = 10/100

else:
    print(f"Khong duoc giam gia")

tongTien = tienVeThang * soThangMuonMua - (tienVeThang*soThangMuonMua)*giamGia

print(f"So tien phai tra la: {tongTien:{'.'}0f} VND")