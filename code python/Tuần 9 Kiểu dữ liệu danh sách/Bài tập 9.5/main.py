# Yêu cầu:
# 1. nhập n
# 2. nhập 1 chuỗi string 
# (chứa toàn là số, mỗi số cách nhau 1 dấu cách)

# 3. nhập 1 chuỗi string 
# (chứa toàn là số, mỗi số cách nhau 1 dấu cách)

# 4. in ra loại nấm có thể ăn được
# 5. in ra loại nấm có độc tốc cao nhất
# 6. sắp xếp tăng dần (theo dinh dưỡng)

# |CHƯƠNG TRÌNH CHÍNH|
n = int(input())

str1 = input()
str2 = input()

# chuyển string sang danh sách
ds1 = str1.split(" ")
ds2 = str2.split(" ")

# chuyển phần tử string
# sang phần tử kiểu int
ds_1 = []
ds_2 = []

for i in range(0, n, 1):
    ds_1.append(int(ds1[i]))
    ds_2.append(int(ds2[i]))

print()

# in ra nấm ăn được
# thì độc_tố * 2 <= dinh_dưỡng
for i in range(0, n, 1):
    if ds_1[i] >= ds_2[i]*2:
        print(f"({ds_1[i]}, {ds_2[i]})", end=" ")

print()


max_doc = max(ds_2)
for i in range(0, n, 1):
    if max_doc == ds_2[i]:
        print(f"({ds_1[i]}, {ds_2[i]})", end=" ")


for i in range(0, n-1, 1):
    for j in range(i+1, n, 1):
        if ds_1[i] > ds_1[j]:
            # thì hoán đổi ds_1
            ds_1[i], ds_1[j] = ds_1[j], ds_1[i]

            # thì hoán đổi ds_2
            ds_2[i], ds_2[j] = ds_2[j], ds_2[i]

# in kết quả sau
# khi sắp xếp tăng dần
# theo dinh dưỡng
print()
for i in range(0, n, 1):
    print(f"({ds_1[i]}, {ds_2[i]})", end=" ")