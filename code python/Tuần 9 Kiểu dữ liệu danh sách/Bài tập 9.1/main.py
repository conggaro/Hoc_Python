# Yêu cầu:
# 1. nhập n
# 2. nhập n phần tử
# 3. tính tổng các số chẵn chia hết cho 3
# 4. đếm số nguyên tố trong dãy
# 5. đếm số chính phương khác nhau có trong dãy

# |CHƯƠNG TRÌNH CHÍNH|
from math import sqrt
from math import floor
from math import pow

n = int(input("Nhap n: "))

ds = []

print()

for i in range(0, n, 1):
    item = int(input(f"Nhap ds[{i}]: "))
    ds.append(item)

tong = 0

for i in range(0, n, 1):
    if ds[i] % 2 == 0 and ds[i] % 3 == 0:
        tong = tong + ds[i]

print(f"\nTong cac so chan chia het cho 3: {tong}")

# hàm kiểm tra số nguyên tố
def KiemTra_SNT(thamSo):
    if thamSo < 2:
        return False
    
    elif thamSo >= 2:
        for i in range(2, floor(sqrt(thamSo)) + 1, 1):
            if thamSo % i == 0:
                return False
            
        return True

dem_SNT = 0

for i in range(0, n, 1):
    if KiemTra_SNT(ds[i]) == True:
        dem_SNT = dem_SNT + 1

print(f"So luong so nguyen to la: {dem_SNT}")

# hàm kiểm tra số chính phương
def KiemTra_SCP(thamSo):
    if pow(floor(sqrt(thamSo)), 2) == thamSo:
        return True
    
    else:
        return False
    
ds_SCP = []

for i in range(0, n, 1):
    if KiemTra_SCP(ds[i]) == True:
        ds_SCP.append(ds[i])

ds_SCP.sort()

ds1 = []

for item in ds_SCP:
    if item not in ds1:
        ds1.append(item)

print(f"So luong so chinh phuong khac nhau la: {len(ds1)}")