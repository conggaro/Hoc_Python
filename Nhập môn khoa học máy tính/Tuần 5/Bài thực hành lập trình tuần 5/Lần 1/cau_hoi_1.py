# Yêu cầu:
# 1. nhập n
# 2. in ra hình vẽ

n = int(input())

kyTu = "*"

for i in range(1, n + 1, 1):
    print(f" {kyTu:{' '}^{n*2}}")
    kyTu = kyTu + "**"
print()

kyTu2 = "*****"
for i in range(0, n, 1):
    print(f"{kyTu2}")
print()

kyTu3 = "*"

for i in range(0, n, 1):
    print(f"{kyTu3:<{n*2}}")
    
    if i != n - 1:
        kyTu3 = kyTu3 + "**"

index = len(kyTu3)      # bằng 9 nếu n = 5

kyTu4 = ""
so = 2          # cái số để hỗ trợ trừ thôi

for i in range(n - 2, -1, -1):
    index = index - 2
    kyTu4 = kyTu3[0: index]
    print(kyTu4)