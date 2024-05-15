"""
Định nghĩa số nguyên tố:
Số nguyên tố là số tự nhiên lớn hơn 1,
chỉ có hai ước là 1 và chính nó.

Các số nguyên tố nhỏ hơn 10 là 2; 3; 5; 7.
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


# hàm kiểm tra số nguyên tố
def KiemTra_SoNguyenTo(parameter):
    result = True

    if parameter <= 1:
        return False

    start = 2
    end = (parameter // 2) + 1

    for i in range(start, end):
        if parameter % i == 0:
            result = False
            break

    return result


# hàm lấy ra danh sách số nguyên tố
# trong khoảng từ m đến n
def Lay_DanhSach_SoNguyenTo(m, n):
    result = []

    start = m
    end = n + 1

    for i in range(start, end):
        if KiemTra_SoNguyenTo(i):
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

# kiểm tra m có là số nguyên tố không
check1 = f"{m} là số nguyên tố" if KiemTra_SoNguyenTo(m) else f"{m} không là số nguyên tố"
print(check1)

# xuống dòng
print()

# kiểm tra n có là số nguyên tố không
check2 = f"{n} là số nguyên tố" if KiemTra_SoNguyenTo(n) else f"{n} không là số nguyên tố"
print(check2)

# xuống dòng
print()

# lấy danh sách số nguyên tố
listPrimeNumber = []

if m <= n:
    listPrimeNumber = Lay_DanhSach_SoNguyenTo(m, n)
    print(f"Danh sách số nguyên tố: {listPrimeNumber}")
    print(f"Có {len(listPrimeNumber)} số nguyên tố")
else:
    print(f"Danh sách số nguyên tố: {listPrimeNumber}")
    print(f"Có {len(listPrimeNumber)} số nguyên tố")
