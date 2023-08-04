def tong(a, b):
    return a + b

def tongDaySo(n):
    ketQua = 0

    for i in range(0, n + 1):
        ketQua = tong(ketQua, i)

    return ketQua

k = tongDaySo(10)

print(k)