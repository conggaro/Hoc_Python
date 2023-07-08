# Yêu cầu:
# 1. nhập n
# 2. vẽ tam giác bằng dấu "*"

n = int(input("Nhap n: "))

item = "*"

for i in range(0, n, 1):
    print(f"{item:{' '}>{n * 2}}")
    item = item + "**"

vi_tri = len(item) - 2

for i in range(0, n - 1, 1):
    vi_tri = vi_tri - 2
    print(f"{item[0: vi_tri: 1]:{' '}>{n * 2}}")