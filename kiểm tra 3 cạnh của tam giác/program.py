import math

# hàm nhập số từ bàn phím
# nếu nhập sai thì yêu cầu nhập lại
def Enter_TheNumber(message):
    number = input(message)

    while(True):
        if Check_TheNumber(number):
            break
        else:
            number = input("Hãy nhập lại: ")

    return float(number)


# hàm kiểm tra số
def Check_TheNumber(parameter):
    try:
        float(parameter)
        return True
    except ValueError:
        return False


# hàm kiểm tra 3 cạnh của 1 tam giác
def Check_Three_Sides_Of_TheTriangle(x, y, z):
    condition1 = True if x + y > z else False
    condition2 = True if x + z > y else False
    condition3 = True if y + z > x else False

    if condition1 and condition2 and condition3:
        return True
    else:
        return False


# hàm tính diện tích của hình tam giác
# theo công thức Hê-rông
def Calculate_TheArea_Of_A_Triangle(x, y, z):
    p = (x + y + z) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s


# nhập 3 cạnh của tam giác
text1 = "Nhập cạnh a: "
text2 = "Nhập cạnh b: "
text3 = "Nhập cạnh c: "

a = Enter_TheNumber(text1)
b = Enter_TheNumber(text2)
c = Enter_TheNumber(text3)


# xuống dòng
print()


# kiểm tra 3 cạnh vừa nhập
# có phải là 3 cạnh của 1 tam giác không
if Check_Three_Sides_Of_TheTriangle(a, b, c):
    print(f"{a}, {b}, {c} là 3 cạnh của 1 tam giác.")

    theArea = Calculate_TheArea_Of_A_Triangle(a, b, c)
    print(f"\nDiện tích: {theArea}")
else:
    print(f"{a}, {b}, {c} không là 3 cạnh của 1 tam giác.")