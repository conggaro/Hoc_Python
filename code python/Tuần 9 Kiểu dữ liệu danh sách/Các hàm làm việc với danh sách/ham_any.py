ds = [1, 2, 3, 5, 0]
print(any(ds))
# kết quả:
# True


ds = [0, False]
print(any(ds))
# kết quả:
# False


ds = [0, False, 8]
print(any(ds))
# kết quả:
# True


ds = []
print(any(ds))
# kết quả:
# False