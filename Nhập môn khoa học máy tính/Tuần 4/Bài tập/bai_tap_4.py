# Yêu cầu:
# 1. nhập cân nặng (trọng lượng)
# 2. nhập chiều cao

# 3. tính BMI
# 4. in ra kết quả cơ thể

# BMI = cân nặng (kg) / chiều cao (mét)

# BMI < 18.5                    --> Gầy
# 18.5 <= BMI and BMI < 23      --> Bình thường
# 23 <= BMI and BMI < 25        --> Tiền béo phì
# 25 <= BMI and BMI <= 30       --> Béo phì độ 1
# 30 < BMI                      --> Béo phì độ 2

import math

canNang = float(input(f"Nhap can nang (kg): "))

chieuCao = float(input(f"Nhap chieu cao (m): "))

BMI = canNang / math.pow(chieuCao, 2)

if BMI < 18.5:
    print(f"Ket qua: {BMI:{'.'}3f}\nBan gay.")

elif 18.5 <= BMI and BMI < 23:
    print(f"Ket qua: {BMI:{'.'}3f}\nBan binh thuong.")

elif 23 <= BMI and BMI < 25:
    print(f"Ket qua: {BMI:{'.'}3f}\nBan tien beo phi.")

elif 25 <= BMI and BMI <= 30:
    print(f"Ket qua: {BMI:{'.'}3f}\nBan beo phi do 1.")

elif 30 < BMI:
    print(f"Ket qua: {BMI:{'.'}3f}\nBan beo phi do 2.")