# Yêu cầu:
# 1. nhập n
# 2. tính sa        (lấy 3 chữ số thập phân)
# 3. tính sb        (lấy 3 chữ số thập phân)

n = int(input())

sa = 0
sb = 1

for i in range(1, n + 1, 1):
    sa = sa + i**2
    sb = sb + 1/(i*(i + 1))

print(f"{sa:{'.'}3f}")
print(f"{sb:{'.'}3f}")