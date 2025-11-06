
def fibonacci_sequence(start_sequence, length):
    if length == 0:
        return []
    if length == 1:
        return [start_sequence[0]]
    
    result = start_sequence
    while len(result) < length:
        next_value = result[-2] + result[-1]
        result.append(next_value)

    return result



