
def to_decimal(binary):
    result = 0
    reversed_binary = binary[::-1]
    for i, x in enumerate(reversed_binary):
        bit = int(x)
        if bit:
            result += 2 ** i
    return result



