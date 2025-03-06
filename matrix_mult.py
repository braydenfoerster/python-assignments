def dot_prod(a, b):
    result = 0
    i = 0
    while i < len(a):
        result = result + (a[i] * b[i])  # Only adding
        i = i + 1  # Increment index
    return result


def matrix_mult(m1, m2):
    if len(m1[0]) != len(m2):  # Check if multiplication is possible
        return None

    final_matrix = []  # This will hold the answer at the end
    for row in m1:  # Loop through each row of first matrix
        new_row = []  # This will hold the row result
        j = 0
        while j < len(m2[0]):  # This is to go through each column of second matrix
            col = []  # Store the column values
            i = 0
            while i < len(m2):  # Loop through rows to get the column
                col.append(m2[i][j])
                i = i + 1  # Increment manually
            new_row.append(dot_prod(row, col))  # Using the dot product function
            j = j + 1  # Move to the next column
        final_matrix.append(new_row)  # Add completed row to the matrix

    return final_matrix


# Example
matrix_A = [[3, 1], [-8, 5], [1, 4]]
matrix_B = [[1, 4, 7, 1], [-5, -8, 4, 3]]
print(matrix_mult(matrix_A, matrix_B))
