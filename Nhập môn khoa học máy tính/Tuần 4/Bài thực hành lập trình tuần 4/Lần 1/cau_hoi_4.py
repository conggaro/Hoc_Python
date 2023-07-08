# Yêu cầu:
# 1. nhập tháng
# 2. nhập năm
# 3. in ra số lượng ngày của tháng đó

# hàm kiểm tra năm nhuận
def KiemTra_NamNhuan(thamSo):
    kiemTra1 = True if thamSo % 400 == 0 else False
    kiemTra2 = True if thamSo % 4 == 0 else False
    kiemTra3 = True if thamSo % 100 != 0 else False

    # năm nhuận thì chia hết cho 400
    # hoặc chia hết cho 4 và không chia hết cho 100
    if kiemTra1 or (kiemTra2 and kiemTra3):
        return True
    else:
        return False
    
thang = int(input())

nam = int(input())

if KiemTra_NamNhuan(nam) == True:
    if thang == 1:
        print(31)
    
    elif thang == 2:
        print(29)

    elif thang == 3:
        print(31)

    elif thang == 4:
        print(30)

    elif thang == 5:
        print(31)

    elif thang == 6:
        print(30)

    elif thang == 7:
        print(31)

    elif thang == 8:
        print(31)

    elif thang == 9:
        print(30)

    elif thang == 10:
        print(31)

    elif thang == 11:
        print(30)

    elif thang == 12:
        print(31)

elif KiemTra_NamNhuan(nam) == False:
    if thang == 1:
        print(31)
    
    elif thang == 2:
        print(28)

    elif thang == 3:
        print(31)

    elif thang == 4:
        print(30)

    elif thang == 5:
        print(31)

    elif thang == 6:
        print(30)

    elif thang == 7:
        print(31)

    elif thang == 8:
        print(31)

    elif thang == 9:
        print(30)

    elif thang == 10:
        print(31)

    elif thang == 11:
        print(30)

    elif thang == 12:
        print(31)