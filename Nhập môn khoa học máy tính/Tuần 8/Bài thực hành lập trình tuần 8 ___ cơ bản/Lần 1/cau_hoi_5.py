# Yêu cầu:
# 1. nhập chuỗi a
# 2. nhập chuỗi b
# 3. in ra "co" hoặc "khong"

# tức là kiểm tra thuật ngữ Anagram

# chương trình chính
a = input()
b = input()

kiemTra = False

if len(a) >= len(b):
    # duyệt phần tử theo biến a
    for i in range (0, len(a), 1):
        if (a[i] in b) == True:
            kiemTra = True

        elif (a[i] in b) == False:
            kiemTra = False
            break

elif len(a) < len(b):
    # duyệt phần tử theo biến b
    for i in range (0, len(b), 1):
        if (b[i] in a) == True:
            kiemTra = True

        elif (b[i] in a) == False:
            kiemTra = False
            break

if kiemTra == True:
    print(f"co")

else:
    print(f"khong")