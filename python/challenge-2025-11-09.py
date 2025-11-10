
def find_word(matrix, word):
    result = []
    n_rows = len(matrix)
    for i in range(n_rows):
        # search row: left to right
        row = matrix[i]
        row_string = "".join(row)
        column_indices = find_word_in_string(row_string, word)
        if column_indices:
            j1, j2 = column_indices
            result = [[i, j1], [i, j2]]
            return result
        # search row: right to left
        row_reversed = row[::-1]
        row_string = "".join(row_reversed)
        column_indices = find_word_in_string(row_string, word)
        if column_indices:
            j1 = len(row_reversed) - column_indices[0] - 1
            j2 = len(row_reversed) - column_indices[1] - 1
            result = [[i, j1], [i, j2]]
            return result
    # search columns of the original by searching rows of the transpose
    matrix_transposed = transpose(matrix)
    n_rows = len(matrix_transposed)
    for i in range(n_rows):
        # search row: left to right
        row = matrix_transposed[i]
        row_string = "".join(row)
        column_indices = find_word_in_string(row_string, word)
        if column_indices:
            j1, j2 = column_indices
            result = [[j1, i], [j2, i]]
            return result
        # search row: right to left
        row_reversed = row[::-1]
        row_string = "".join(row_reversed)
        column_indices = find_word_in_string(row_string, word)
        if column_indices:
            j1 = len(row_reversed) - column_indices[0] - 1
            j2 = len(row_reversed) - column_indices[1] - 1
            result = [[j1, i], [j2, i]]
            return result
    return result

def transpose(matrix):
    result = []
    n_rows = len(matrix)
    n_columns = len(matrix[0])
    for j in range(n_columns):
        row = n_rows * [""]
        result.append(row)
    for i in range(n_rows):
        for j in range(n_columns):
            result[j][i] = matrix[i][j]
    return result

def find_word_in_string(string, word):
    if word not in string:
        return []
    
    difference = len(string) - len(word)
    start = 0
    while start <= difference:
        end = start + len(word)
        selection = string[start:end]
        if selection == word:
            return [start, end - 1]
        start += 1



