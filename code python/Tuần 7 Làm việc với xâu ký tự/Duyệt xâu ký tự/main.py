data1 = "Hello123"
data2 = "Hi456"

# cái loại này
# giống for-each
for item in data1:
    print(item, end=" ")

print()

# còn cái loại này
# là for bình thường
for i in range(0, len(data2), 1):
    print(data2[i], end=" ")