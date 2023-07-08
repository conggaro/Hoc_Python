# Yêu cầu:
# 1. nhập cân nặng (đơn vị kg)
# 2. nhập chiều cao (đơn vị mét)
# 3. in ra đánh giá

# công thức tính BMI
# BMI = cân_nặng / (chiều_cao ^ 2)

can_nang = float(input())

chieu_cao = float(input())

BMI = can_nang / chieu_cao**2

if BMI < 18.5:
    print(f"Loai 1: Gay")

elif 18.5 <= BMI and BMI < 23:
    print(f"Loai 2: Binh thuong")

elif 23 <= BMI and BMI < 25:
    print(f"Loai 3: Tien beo phi")

elif 25 <= BMI and BMI <= 30:
    print(f"Loai 4: Beo phi do 1")

elif 30 < BMI:
    print(f"Loai 5: Beo phi do 2")