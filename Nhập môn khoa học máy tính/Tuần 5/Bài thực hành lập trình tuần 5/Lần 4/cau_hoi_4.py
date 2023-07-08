# Yêu cầu:
# 1. nhập n
# 2. in ra n theo thứ tự ngược lại

n = input()

data = ""

for i in range(len(n) - 1, -1,- 1):
    data = data + n[i]

print(f"{int(data)}")