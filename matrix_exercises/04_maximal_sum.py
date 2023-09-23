# def find_submatrix(matrix, start_row, start_column, subm_w, subm_h):
#     matrix_width = len(matrix[0])
#     matrix_height = len(matrix[0][0])
#     if matrix_width > subm_w and matrix_height > subm_h:
#         submatrix = []
#         for row_index in range(matrix_width - subm_w):
#             row = []
#             for col_index in range(matrix_height - subm_h):
#                 pass
#         return submatrix
#     elif matrix_width == subm_w and matrix_height == subm_h:
#         return matrix
#     else:
#         return 'Given matrix smaller than the submatrix you are trying to extract.'


def extract_submatrix(my_matrix, start_row, start_col, submatrix_width, submatrix_height):
    if (
            start_row < 0
            or start_col < 0
            or start_row + submatrix_height > len(my_matrix)
            or start_col + submatrix_width > len(my_matrix[0])
    ):
        raise ValueError("Indices out of matrix!")
    sub_matrix = []
    for i in range(start_row, start_row + submatrix_height):
        sub_row = []
        for j in range(start_col, start_col + submatrix_width):
            sub_row.append(my_matrix[i][j])
        sub_matrix.append(sub_row)
    return sub_matrix


def matrix_sum(some_matrix):
    sum_of_matrix = 0
    for current_row in some_matrix:
        sum_of_matrix += sum(current_row)
    return sum_of_matrix


rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
max_sum = 0
max_matrix = []
for row in range(rows - 2):
    for column in range(columns - 2):
        submatrix = extract_submatrix(matrix, row, column, 3, 3)
        current_sum = matrix_sum(submatrix)
        if current_sum >= max_sum:
            max_sum = current_sum
            max_matrix = submatrix
print(f'Sum = {max_sum}')
for row in max_matrix:
    print(*row)

