SoLuong = 12
DonGia = 150000

TongTien = SoLuong * DonGia

if SoLuong >= 15:
    TongTien *= 0.7

elif SoLuong >= 10:
    TongTien *= 0.85

else:
    TongTien *= 0.95

print(TongTien)