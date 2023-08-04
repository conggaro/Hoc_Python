# Yêu cầu:
# 1. nhập n
# 2. nhập n phần tử
# 3. đếm người bị béo phì

# |CHƯƠNG TRÌNH CHÍNH|
n = int(input())

ds = []

for i in range(0, n, 1):
    chieu_cao = float(input())
    can_nang = float(input())

    item = [chieu_cao, can_nang]

    ds.append(item)

dem_BeoPhi = 0

# hàm tính BMI
def Ham_Tinh_BMI(chieu_cao, can_nang):
    return can_nang / (chieu_cao**2)

for i in range(0, n, 1):
    if Ham_Tinh_BMI(ds[i][0], ds[i][1]) >= 30:
        dem_BeoPhi = dem_BeoPhi + 1

print(dem_BeoPhi)