mat_khau = input()

dem_ChuThuong = dem_ChuHoa = dem_So = dem_KyTu = 0

kiemTra = False

danhSach_KyTu = "@#$%!"

for item in mat_khau:
    if item.islower():
        dem_ChuThuong += 1
    
    elif item.isupper():
        dem_ChuHoa += 1

    elif item.isdigit():
        dem_So += 1

    elif item in danhSach_KyTu:
        dem_KyTu += 1

if dem_ChuThuong > 0 and dem_ChuHoa > 0 and dem_So > 0 and dem_KyTu > 0:
    kiemTra = True

if len(mat_khau) >= 8 and kiemTra == True:
    print(f"Day la mat khau manh")

else:
    print(f"Day la mat khau yeu")