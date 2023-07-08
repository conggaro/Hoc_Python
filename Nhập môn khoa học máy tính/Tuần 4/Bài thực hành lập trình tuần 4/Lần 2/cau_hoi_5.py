# Yêu cầu:
# 1. nhập số phút
# 2. tính tiền điện thoại

# phí thuê bao bắt buộc là 150000
# => mở máy lên gọi là tự động mất 150000

# 600đ cho mỗi phút gọi của 50 phút đầu tiên
# 400đ cho mỗi phút gọi của 150 phút tiếp theo
# 200đ cho mỗi phút gọi của các phút tiếp theo

so_phut = int(input())

tien = 150000

if so_phut <= 50:
    tien = tien + so_phut * 600
    print(f"{tien:{'.'}0f}")

elif 50 < so_phut and so_phut <= 200:
    tien = tien + 50*600 + (so_phut - 50)*400
    print(f"{tien:{'.'}0f}")

elif 200 < so_phut:
    tien = tien + 50*600 + (200 - 50)*400 + (so_phut - 200)*200
    print(f"{tien:{'.'}0f}")