# input: là nhập vào số nguyên

giay = int(input("Nhap vao so giay: "))

# đổi sang ngày
ngay = giay // 60 // 60 // 24

# tìm giờ thừa
gio = (giay // 60 // 60) - 7 * 24

# tìm phút thừa
phut = (giay // 60) - gio * 60 - ngay * 24 * 60

# tìm giây thừa
giay_thua = giay - (ngay*24*60*60) - (gio*60*60) - phut*60

print(str(giay) + " giay = " + str(ngay) + " ngay " + str(gio) + " gio " \
                + str(phut) + " phut " + str(giay_thua) + " giay")