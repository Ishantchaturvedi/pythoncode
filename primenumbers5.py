def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_count = 0
num = 2

while prime_count < 5:
    if is_prime(num):
        print(num)
        prime_count += 1
    num += 1
