# Yêu cầu:
# 1. nhập số phút
# 2. tính tiền

# Phí thuê bao bắt buộc là 150000đ
# tức là mở máy lên alo 1 phát là mất luôn 150000đ

# 600đ cho mỗi phút gọi của 50 phút đầu tiên
# 400đ cho mỗi phút gọi của 150 phút tiếp theo
# 200đ cho mỗi phút gọi của các phút tiếp theo

so_phut = int(input())

tien = 150000

if so_phut <= 50:
    tien += so_phut * 600
    print(f"{tien}")

elif 50 < so_phut and so_phut <= 200:
    tien += 50 * 600 + (so_phut - 50) * 400
    print(f"{tien}")

elif 200 < so_phut:
    tien += 50*600 + (200 - 50)*400 + (so_phut - 200)*200
    print(f"{tien}")