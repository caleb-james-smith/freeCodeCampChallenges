
def one_hundred(chars):
    result = ""
    target = 100
    while len(result) < target:
        result += chars
    result = result[:target]
    return result



