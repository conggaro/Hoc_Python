x = 5

def F1(y):
    # global x        # muốn tường minh thì thêm "global x"
    y = x + 1
    print(y)    # in ra 6
    return y

def F2():
    x = 10          # x này là biến cục bộ
    x = x + F1(x)   # chỗ này là 10 + 6 = 16
    return x

x = F2()

print(x)