import math

"""
Định nghĩa số chính phương:
Số chính phương là số tự nhiên
có căn bậc hai là một số tự nhiên,

Hay nói cách khác,
số chính phương bằng bình phương
của một số nguyên.

Các số chính phương nhỏ hơn 10 là 0, 1, 4, 9

Số 0 có là số chính phương (đã tra google)
"""

# hàm nhập số nguyên và kiểm tra
# nếu nhập ký tự khác số nguyên
# thì yêu cầu nhập lại
def Nhap_SoNguyen(message):
    value = input(message)

    while(True):
        if KiemTra_SoNguyen(value):
            break
        else:
            value = input("Vui lòng nhập lại: ")

    return int(value)


# hàm kiểm tra số nguyên
def KiemTra_SoNguyen(parameter):
    try:
        int(parameter)
        return True
    except ValueError:
        return False


# hàm kiểm tra số chính phương
def KiemTra_SoChinhPhuong(parameter):
    result = True

    if parameter < 0:
        return False

    sqrt = parameter ** (1/2)

    if math.floor(sqrt) ** 2 != parameter:
        return False

    return result


# hàm lấy ra danh sách số chính phương
# trong khoảng từ m đến n
def Lay_DanhSach_SoChinhPhuong(m, n):
    result = []

    start = m
    end = n + 1

    for i in range(start, end):
        if KiemTra_SoChinhPhuong(i):
            result.append(i)

    return result


# nhập số nguyên m
message1 = "Nhập số nguyên m: "
m = Nhap_SoNguyen(message1)

# xuống dòng
print()

# nhập số nguyên n
message2 = "Nhập số nguyên n: "
n = Nhap_SoNguyen(message2)

# xuống dòng
print()

# kiểm tra m có là số chính phương không
check1 = f"{m} là số chính phương" if KiemTra_SoChinhPhuong(m) else f"{m} không là số chính phương"
print(check1)

# xuống dòng
print()

# kiểm tra n có là số chính phương không
check2 = f"{n} là số chính phương" if KiemTra_SoChinhPhuong(n) else f"{n} không là số chính phương"
print(check2)

# xuống dòng
print()

# lấy danh sách số chính phương
listSquareNumber = []

if m <= n:
    listSquareNumber = Lay_DanhSach_SoChinhPhuong(m, n)
    print(f"Danh sách số chính phương: {listSquareNumber}")
    print(f"Có {len(listSquareNumber)} số chính phương")
else:
    print(f"Danh sách số chính phương: {listSquareNumber}")
    print(f"Có {len(listSquareNumber)} số chính phương")