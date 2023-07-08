# Yêu cầu:
# 1. nhập vào số điện
# 2. tính tiền điện

# [0, 50]       --> 1678 giá bán/1 số
# [51, 100]     --> 1734 giá bán/1 số
# [101, 200]    --> 2014
# [201, 300]    --> 2536
# [301, 400]    --> 2834
# > 400         --> 2927

# ví dụ: 
# số điện tiêu thụ là 170 số điện
# thì số điện cần trả là:
# t = 50 * 1678 + 50 * 1734 + 70 * 2014 = 311580

so_dien = int(input())

if 0 <= so_dien and so_dien <= 50:
    tien = so_dien * 1678
    print(f"{tien}")

elif 50 < so_dien and so_dien <= 100:
    tien = 50 * 1678 + (so_dien - 50) * 1734
    print(f"{tien}")

elif 100 < so_dien and so_dien <= 200:
    tien = 50 * 1678 + (100 - 50) * 1734 + (so_dien - 100) * 2014
    print(f"{tien}")

elif 200 < so_dien and so_dien <= 300:
    tien = 50 * 1678 + (100 - 50) * 1734 + (200 - 100) * 2014 + \
            (so_dien - 200) * 2536
    print(f"{tien}")

elif 300 < so_dien and so_dien <= 400:
    tien = 50 * 1678 + (100 - 50) * 1734 + (200 - 100) * 2014 + \
            (300 - 200) * 2536 + (so_dien - 300) * 2834
    print(f"{tien}")

elif 400 < so_dien:
    tien = 50 * 1678 + (100 - 50) * 1734 + (200 - 100) * 2014 + \
            (300 - 200) * 2536 + (400 - 300) * 2834 + \
            (so_dien - 400) * 2927
    print(f"{tien}")