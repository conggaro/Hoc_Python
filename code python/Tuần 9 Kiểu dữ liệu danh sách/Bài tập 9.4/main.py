# Yêu cầu:
# 1. cho ma trận A (3x4)
# 2. cho ma trận B (3x4)
# 3. tính C = A + B

# ma trận (3x4)
# tức là 3 dòng
# và 4 cột

# |CHƯƠNG TRÌNH CHÍNH|
A = [
    [5, 4, 9, 3],
    [7, 8, 1, 2],
    [9, 3, 6, 8]
]

B = [
    [8, 3, 1, 9],
    [4, 1, 2, 1],
    [2, 1, 5, 6]
]

C = []

for i in range(0, 3, 1):
    item = []

    for j in range(0, 4, 1):
        data = A[i][j] + B[i][j]
        item.append(data)

    C.append(item)

# in kết quả ra màn hình
for i in range(0, 3, 1):
    for j in range(0, 4, 1):
        print(f"{C[i][j]:<5}", end="")

    print()