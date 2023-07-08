# Yêu cầu:
# 1. tìm giá trị vui vẻ lớn nhất

max = 0             # giá trị vui vẻ lớn nhất

ans_x = 0           # thời gian chơi bóng để đạt max
ans_y = 0           # thời gian làm việc để đạt max

for x in range(1, 8 + 1, 1):
    y = 8 - x
    gtvv = 5*x + y

    if 3*x <= y:
        ans_x = x
        ans_y = y

        if max < gtvv:
            max = gtvv

print(f"Thoi gian choi bong: {ans_x}")
print(f"Thoi gian lam viec: {ans_y}")
print(f"Gia tri vui ve cuc dai: {max}")