# Yêu cầu:
# 1. tìm số nhỏ nhất trong dãy số

# cho dãy số a[1], a[2], ..., a[n]

# fake dãy số
a = [1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 2]

# fake n
n = 10

min = a[1]
i = 1

while i <= n:
	if a[i] < min:
		min = a[i]		

	i = i + 1

print(min)