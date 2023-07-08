# Mô tả:
# cho số nguyên dương N
# N <= 10^8 (100 000 000)

# Yêu cầu:
# 1. nhập số N
# 2. kiểm tra số đối xứng

N = input(f"Hay nhap vao 1 so: ")

so_VietNguoc = ""               # số viết ngược lại

for i in range(len(N) - 1, 0 - 1, -1):
    so_VietNguoc = so_VietNguoc + N[i]

# kiểm tra N có phải số đối xứng không
if so_VietNguoc == N:
    print(f"So doi xung")

else:
    print(f"So KHONG doi xung")