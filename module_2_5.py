def get_matrix_walrus(n, m, value):
    """with var columns and walrus operator"""
    matrix = []
    for i in range(n):
        matrix.append(columns := [])
        for j in range(m):
            columns.append(value)
    return matrix


def get_matrix_standard(n, m, value):
    """as stated in the task"""
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


def get_matrix_on_list_generator(n, m, value):
    """with list generator"""
    return [[value for j in range(m)] for i in range(n)]


print("\nWith use walrus operator")
print(result1 := get_matrix_walrus(2, 2, 10))
print(result2 := get_matrix_walrus(3, 5, 42))
print(result3 := get_matrix_walrus(4, 2, 13))
print("\nAs stated in the task")
print(result1 := get_matrix_standard(2, 2, 10))
print(result2 := get_matrix_standard(3, 5, 42))
print(result3 := get_matrix_standard(4, 2, 13))
print("\nList generator")
print(result1 := get_matrix_on_list_generator(2, 2, 10))
print(result2 := get_matrix_on_list_generator(3, 5, 42))
print(result3 := get_matrix_on_list_generator(4, 2, 13))
