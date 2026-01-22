# give true for prime and false for non prime
def is_prime(n):
    i = 0
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True


print(is_prime(7))
print(is_prime(9))
