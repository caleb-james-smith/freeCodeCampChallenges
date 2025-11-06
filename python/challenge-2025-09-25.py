
def second_largest(arr):
    result = float("inf")
    arr.sort(reverse=True)

    assignments = 0
    i = 0
    while assignments < 2:
        if arr[i] < result:
            result = arr[i]
            assignments += 1
        i += 1
    return result
