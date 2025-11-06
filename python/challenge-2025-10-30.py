
def nth_prime(n):
    result = 2
    ith_prime = 1
    while ith_prime < n:
        result += 1
        if is_prime(result):
            ith_prime += 1
    return result

def is_prime(n):
    if n < 2:
        return False
    num_divisors = get_num_divisors(n)
    if num_divisors == 2:
        return True
    else:
        return False

def get_num_divisors(n):
    result = 0
    for i in range(1, n + 1):
        if n % i == 0:
            result += 1
    return result



