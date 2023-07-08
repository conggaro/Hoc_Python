# Yêu cầu:
# 1. nhập số điện
# 2. in ra tiền điện

so_dien = int(input())

tien = 0

if 0 <= so_dien and so_dien <= 50:
    tien += so_dien * 1678

elif 51 <= so_dien and so_dien <= 100:
    tien += 50*1678 + (so_dien - 50)*1734

elif 101 <= so_dien and so_dien <= 200:
    tien += 50*1678 + (100 - 50)*1734 + (so_dien - 100)*2014

elif 201 <= so_dien and so_dien <= 300:
    tien += 50*1678 + (100 - 50)*1734 + (200 - 100)*2014 + \
                (so_dien - 200)*2536
    
elif 301 <= so_dien and so_dien <= 400:
    tien += 50*1678 + (100 - 50)*1734 + (200 - 100)*2014 + \
                (300 - 200)*2536 + (so_dien - 300)*2834
    
elif 400 < so_dien:
    tien += 50*1678 + (100 - 50)*1734 + (200 - 100)*2014 + \
                (300 - 200)*2536 + (400 - 300)*2834 + (so_dien - 400)*2927

print(f"{tien}")