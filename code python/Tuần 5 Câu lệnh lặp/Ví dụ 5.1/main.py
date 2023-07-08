# Yêu cầu:
# 1. nhập vào tuổi
# 2. in ra "Ban khong con tre" hoặc "Ban van tre"

a = int(input("Nhap vao so tuoi cua ban: "))

while a <= 0:
    a = int(input("Tuoi > 0, nhap lai tuoi: "))

if a < 40:
    print(f"Ban van tre")

else:
    print(f"Ban khong con tre")