# Yêu cầu:
# 1. nhập ngày
# 2. nhập tháng
# 3. nhập năm

# 4. in ra hôm qua
# 5. in ra ngày mai

import datetime

# Nhập ngày, tháng, năm
day = int(input())
month = int(input())
year = int(input())

# Khởi tạo đối tượng datetime từ ngày, tháng, năm vừa nhập
dt_datetime = datetime.datetime(year, month, day)

# Tính toán hôm qua và in ra kết quả
yesterday = dt_datetime - datetime.timedelta(days=1)
print(yesterday.strftime("%d/%m/%Y"))

# Tính toán ngày mai và in ra kết quả
tomorrow = dt_datetime + datetime.timedelta(days=1)
print(tomorrow.strftime("%d/%m/%Y"))