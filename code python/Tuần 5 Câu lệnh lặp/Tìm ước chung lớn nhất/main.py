# Yêu cầu:
# 1. nhập vào số bác sĩ
# 2. nhập vào số y tá
# 3. tính số nhóm cực đại có thể chia

a = int(input("Nhap vao so bac si: "))

b = int(input("Nhap vao so y ta: "))

while a != b:
    if a > b:
        a = a - b

    elif a < b:
        b = b - a
    
# lặp đến lúc a và b bằng nhau thì thôi
# chắc chắn sẽ có lúc bằng nhau
# nếu bằng nhau thì dừng vòng lặp while
n = a

print(f"So nhom chia duoc la: {n}")