# Yêu cầu:
# 1. nhập số nguyên a
# 2. nhập số nguyên b
# 3. nhập số nguyên c
# 4. nhập số nguyên d
# 5. in ra số lớn thứ 2

a = int(input())
b = int(input())
c = int(input())
d = int(input())

danh_sach = [a, b, c, d]

max = danh_sach[0]

for item in danh_sach:
    if max < item:
        max = item
    
max2 = danh_sach[0]

for item in danh_sach:
    if item != max:
        if max2 < item:
            max2 = item

print(f"{max2}")