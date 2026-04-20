def nth_prime(n):
    max_val = 10
    primes = get_primes(max_val)
    while len(primes) < n:
        max_val *= 10
        primes = get_primes(max_val)
    result = primes[n - 1]
    return result

def get_primes(max_val):
    primes = []
    for n in range(2, max_val + 1):
        if is_prime(n):
            primes.append(n)
    return primes

def is_prime(n):
    divisors = get_divisors(n)
    num_divisors = len(divisors)
    if n > 1 and num_divisors == 2:
        return True
    else:
        return False

def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)            
    return divisors
