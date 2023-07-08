# Yêu cầu:
# 1. nhập số nguyên a
# 2. nhập số nguyên b
# 3. nhập số nguyên c
# 4. nhập số nguyên d

# 5. in ra số nhỏ nhất
# 6. in ra số lớn nhất

a = int(input())
b = int(input())
c = int(input())
d = int(input())

danhSach = [a, b, c, d]

min = danhSach[0]
max = danhSach[0]

for item in danhSach:
    if min > item:
        min = item
    
    if max < item:
        max = item

print(f"{min}")
print(f"{max}")