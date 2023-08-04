# Yêu cầu:
# 1. nhập n
# 2. nhập n phần tử
# 3. in ra max
# 4. in ra min
# 5. in ra tổng của tất cả phần tử

# |CHƯƠNG TRÌNH CHÍNH|
n = int(input())

ds = []

for i in range(0, n, 1):
    item = int(input())

    ds.append(item)

print(max(ds))
print(min(ds))
print(sum(ds))