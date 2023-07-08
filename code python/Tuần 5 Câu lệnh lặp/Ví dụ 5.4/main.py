# Yêu cầu:
# 1. in ra bảng cửu chương

print(f"\t", end="")
for i in range(1, 10 + 1, 1):
    print(f"{i}\t", end="")

print(end="\n")

for i in range(1, 10 + 1, 1):
    print(f"{i}\t", end="")

    for j in range(1, 10 + 1, 1):
        print(f"{i * j}\t", end="")

    print(end="\n")