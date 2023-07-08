# Yêu cầu:
# 1. nhập a
# 2. nhập b
# 3. nhập c
# 4. nhập d
# 5. in ra BCNN(a, b, c, d)

a = int(input())
b = int(input())
c = int(input())
d = int(input())

# index bắt đầu
index_bat_dau = max(a, b, c, d)

# index kết thúc
index_ket_thuc = a * b * c * d

BCNN = 0

for i in range(index_bat_dau, index_ket_thuc + 1, 1):
    kiemTra1 = True if i % a == 0 else False
    kiemTra2 = True if i % b == 0 else False
    kiemTra3 = True if i % c == 0 else False
    kiemTra4 = True if i % d == 0 else False

    if kiemTra1 and kiemTra2 and kiemTra3 and kiemTra4:
        BCNN = i
        break

print(f"{BCNN}")