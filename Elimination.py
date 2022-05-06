# Gaussian Elimination with Scaled Pivoting
def gauss_elimination(matrix):
    """
    Gaussian Elimination with Scaled Pivoting
    """
    n = len(matrix)
    for i in range(n):
        # Find the maximum element in the column
        max_el = abs(matrix[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > max_el:
                max_el = abs(matrix[k][i])
                max_row = k
        # Swap the row with the maximum element
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        # Perform elimination
        for k in range(i + 1, n):
            c1 = matrix[k][i] / GCD(matrix[i][i], matrix[k][i])
            c2 = matrix[i][i] / GCD(matrix[i][i], matrix[k][i])
            for j in range(i, n):
                if i == j:
                    matrix[k][j] = 0
                else:
                    matrix[k][j] = -c1 * matrix[i][j] + c2 * matrix[k][j]
    return matrix

# find the greatest common digit of two numbers
def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


matrix = [[9, 5, 1],
          [3, 7, 2],
          [1, 8, 4]]
print(gauss_elimination(matrix))