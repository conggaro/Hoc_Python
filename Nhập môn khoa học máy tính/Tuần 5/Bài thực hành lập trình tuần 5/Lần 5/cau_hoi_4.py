# Yêu cầu:
# 1. nhập n
# 2. in ra "Co" hoặc "Khong"

# nếu là số amstrong thì in ra có

# số amstrong kiểu:
# n có k chữ số
# tổng của các chữ số mũ k mà bằng n
# => thì gọi là số amstrong

n = input()

k = len(n)

tong = 0

for i in range(0, k, 1):
    tong = tong + int(n[i])**k

if tong == int(n):
    print(f"Co")

else:
    print("Khong")