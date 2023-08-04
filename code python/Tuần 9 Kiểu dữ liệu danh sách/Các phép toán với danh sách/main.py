# phép toán +
ds1 = [1, 2]
ds2 = [3, 4, 5]
ds3 = ds1 + ds2
print(ds3)          # kết quả: [1, 2, 3, 4, 5]


# phép toán *
ds4 = ["AA", "BB", "CC"]
ds5 = ds4 * 2
print(ds5)          # kết quả: ['AA', 'BB', 'CC', 'AA', 'BB', 'CC']


# phép toán in
kiemTra1 = 1 in ds1
kiemTra2 = 3 in ds1
print(f"\nCo so 1 trong ds1: {kiemTra1}")
print(f"Co so 3 trong ds1: {kiemTra2}")


# phép toán not in
kiemTra3 = 1 not in ds1
kiemTra4 = 3 not in ds1
print(f"\nKhong co so 1 trong ds1: {kiemTra3}")
print(f"Khong co so 3 trong ds1: {kiemTra4}")


# phép toán is
# dùng để kiểm tra 2 danh sách
# có chung một địa chỉ không
ds_A = [1, 2]
ds_B = [1, 2]
kiemTra_DiaChi1 = ds_A is ds_B
if kiemTra_DiaChi1 == True:
    print(f"\nds_A va ds_B chung dia chi")

elif kiemTra_DiaChi1 == False:
    print(f"\nds_A va ds_B khong chung dia chi")

ds_C = [1, 2]
ds_D = ds_C
kiemTra_DiaChi2 = ds_C is ds_D
if kiemTra_DiaChi2 == True:
    print(f"\nds_C va ds_D chung dia chi")

elif kiemTra_DiaChi2 == False:
    print(f"\nds_C va ds_D khong chung dia chi")


# phép toán ==
# dùng để kiểm tra 2 danh sách
# có bằng nhau không 
# (chỉ cần khác 1 phần tử --> thì nó in ra không bằng nhau)
ds_X = [1, 2, 3]
ds_Y = [1, 2, 3]
kiemTra_BangNhau1 = ds_X == ds_Y
if kiemTra_BangNhau1 == True:
    print(f"\nds_X va ds_Y bang nhau")

elif kiemTra_BangNhau1 == False:
    print(f"\nds_X va ds_Y khong bang nhau")

ds_M = [1, 2, 3]
ds_N = [1, 2, 4]
kiemTra_BangNhau2 = ds_M == ds_N
if kiemTra_BangNhau2 == True:
    print(f"\nds_M va ds_N bang nhau")

elif kiemTra_BangNhau2 == False:
    print(f"\nds_M va ds_N khong bang nhau")


# phép toán =
# phép gán danh sách
ds_BanDau = [1, 2, 3]
print(f"\nDanh sach ban dau: {ds_BanDau}")
ds_BanDau = [4, 5, 6]
print(f"Danh sach luc sau: {ds_BanDau}")