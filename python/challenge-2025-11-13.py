
def shift_array(arr, n):
    length = len(arr)
    result = [None] * length
    for i in range(length):
        x = arr[i]
        j = i - n % length
        result[j] = x
    return result



