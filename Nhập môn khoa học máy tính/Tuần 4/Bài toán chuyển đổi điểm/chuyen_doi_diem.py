# Yêu cầu:
# 1. nhập vào điểm số (điểm <= 100)
# 2. chuyển sang chữ

# [90, 100]     --> A
# [80, 90)      --> B
# [70, 80]      --> C
# [60, 70]      --> D
# [0, 60]       --> F

diem = float(input("Nhap vao diem: "))

if 90 <= diem and diem <= 100:
    print(f"A")

elif 80 <= diem and diem < 90:
    print(f"B")

elif 70 <= diem and diem < 80:
    print(f"C")

elif 60 <= diem and diem < 70:
    print(f"D")

elif 0 <= diem and diem < 60:
    print(f"F")