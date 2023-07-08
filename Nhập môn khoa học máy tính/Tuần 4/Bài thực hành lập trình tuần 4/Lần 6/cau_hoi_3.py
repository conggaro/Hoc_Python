# Yêu cầu:
# 1. nhập số phút
# 2. tính tiền

so_phut = int(input())

tien = 150000

if so_phut <= 50:
    tien += so_phut * 600

elif 50 < so_phut and so_phut <= 200:
    tien += 50*600 + (so_phut - 50)*400

elif 200 < so_phut:
    tien += 50*600 + (200 - 50)*400 + (so_phut - 200)*200

print(f"{tien}")