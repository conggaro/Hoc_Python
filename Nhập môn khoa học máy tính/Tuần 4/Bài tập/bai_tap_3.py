# Yêu cầu:
# 1. nhập năm
# 2. kiểm tra xem năm đó có phải năm nhuận không

# năm nhuận thì chia hết cho 400

# hoặc chia hết cho 4 
# nhưng không chia hết cho 100

nam = int(input(f"Nhap nam: "))

kiemTra1 = True if nam % 400 == 0 else False    # năm chia hết cho 400

kiemTra2 = True if nam % 4 == 0 else False      # năm chia hết cho 4

kiemTra3 = True if nam % 100 != 0 else False    # năm không chia hết cho 100

if kiemTra1 == True or (kiemTra2 == True and kiemTra3 == True):
    print(f"Nam {nam} la nam nhuan.")

else:
    print(f"Nam {nam} khong phai nam nhuan.")