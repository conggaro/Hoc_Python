# Yêu cầu:
# 1. nhập vào a
# 2. nhập vào b
# 3. nhập vào c
# 4. nhập vào d

# 5. tìm số nhỏ nhất
# 6. tìm số lớn nhất

a = float(input())

b = float(input())

c = float(input())

d = float(input())

danhSach = [a, b, c, d]

min = a
max = a

for item in danhSach:
    if min > item:
        min = item
    
    if max < item:
        max = item

print(f"{min:{'.'}0f}")

print(f"{max:{'.'}0f}")