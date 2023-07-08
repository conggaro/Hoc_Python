m = int(input())
n = int(input())

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    return count

start = m
end = n

kiemTra1 = True if 500 < m < 100000 else False
kiemTra2 = True if 500 < n and n < 100000 else False

if kiemTra1 == True and kiemTra2 == True:
    prime_count = count_primes(start, end)
    print(prime_count)

else:
    print(f"N/A")