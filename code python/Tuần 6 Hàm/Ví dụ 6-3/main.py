# hàm cộng 2 số
def Ham_Cong_2_So(thamSo1, thamSo2):
    return thamSo1 + thamSo2

# hàm nhập các hệ số a, b, c
def Ham_NhapDuLieu():
    a = float(input("Cho biet he so a: "))
    b = float(input("Cho biet he so b: "))
    c = float(input("Cho biet he so c: "))

    return a, b, c

# hàm thực hiện 4 phép toán
def Ham_PhepToan(a, b):
    tong = a + b
    hieu = a - b
    tich = a * b
    thuong = a / b

    return tong, hieu, tich, thuong

# hàm phương trình có 2 nghiệm
def Ham_Phuong_Trinh_2_Nghiem():
    return 0

# chương trình chính
a, b, c = Ham_NhapDuLieu()