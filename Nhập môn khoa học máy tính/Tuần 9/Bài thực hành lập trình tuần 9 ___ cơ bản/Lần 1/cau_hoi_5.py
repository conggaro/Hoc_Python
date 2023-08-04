# Yêu cầu:
# 1. nhập n
# 2. nhập n phần tử
# 3. in ra số lượng người béo phì

# |CHƯƠNG TRÌNH CHÍNH|
n = int(input())

ds = []

for i in range(0, n, 1):
    chieu_cao = float(input())
    can_nang = float(input())

    item = []

    item.append(chieu_cao)
    item.append(can_nang)

    ds.append(item)

dem = 0

# hàm tính BMI
def Tinh_BMI(chieu_cao, can_nang):
    BMI = can_nang / (chieu_cao**2)

    return BMI

for i in range(0, len(ds), 1):
    if Tinh_BMI(ds[i][0], ds[i][1]) >= 30:
        dem = dem + 1

print(dem)