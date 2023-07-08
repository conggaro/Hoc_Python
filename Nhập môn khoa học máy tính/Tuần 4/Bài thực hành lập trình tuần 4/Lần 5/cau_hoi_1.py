# Yêu cầu:
# 1. nhập vào tháng
# 2. nhập vào năm
# 3. in ra số ngày của tháng đó

thang = int(input())

nam = int(input())

danhSach = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
    danhSach[1] = 29

print(f"{danhSach[thang - 1]}")