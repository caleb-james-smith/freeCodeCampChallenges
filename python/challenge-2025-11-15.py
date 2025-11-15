
def gcd(x, y):
    result = 1
    i = 1
    while i <= x and i <= y:
        if x % i == 0 and y % i == 0:
            result = i
        i += 1
    return result



