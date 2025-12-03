
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def combinations(cards):
    total = 52
    result = int(factorial(total) / (factorial(total - cards) * factorial(cards)))
    return result



