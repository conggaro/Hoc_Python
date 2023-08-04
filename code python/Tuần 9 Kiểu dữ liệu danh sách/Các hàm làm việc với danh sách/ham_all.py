# List chứa toàn giá trị True
danhsach = [6,7,8,9,10]
print(all(danhsach))
# kết quả:
# True


# Tất cả các giá trị của list là False
danhsach = [0, False]
print(all(danhsach))
# kết quả:
# False


# List chứa một giá trị False
danhsach = [10,9,5, 0]
print(all(danhsach))
# kết quả:
# False


# List chứa một giá trị True
danhsach = [0, False, 1]
print(all(danhsach))
# kết quả:
# False


# List rỗng
danhsach = []
print(all(danhsach))
# kết quả:
# True