# Yêu cầu:
# 1. nhập vào n
# 2. in ra n kiểu viết ngược lại

n = int(input())

du_lieu = str(n)        # chuyển từ int sang string

ketQua = ""

for i in range(len(du_lieu) - 1, -1, -1):
    ketQua = ketQua + du_lieu[i]

du_lieu2 = int(ketQua)

print(f"{du_lieu2}")