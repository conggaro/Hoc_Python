# Yêu cầu:
# 1. nhập vào một chuỗi
# 2. chuỗi được mã hóa

# |CHƯƠNG TRÌNH CHÍNH|
s = input()

for item in s:
    if item in "ABC":
        s = s.replace(item, "2")

    elif item in "DEF":
        s = s.replace(item, "3")

    elif item in "GHI":
        s = s.replace(item, "4")

    elif item in "JKL":
        s = s.replace(item, "5")

    elif item in "MNO":
        s = s.replace(item, "6")

    elif item in "PQRS":
        s = s.replace(item, "7")

    elif item in "TUV":
        s = s.replace(item, "8")

    elif item in "WXYZ":
        s = s.replace(item, "9")

print(s)