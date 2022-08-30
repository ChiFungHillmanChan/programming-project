matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2 = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]




def rotate_clockwise(matrix):

    n = len(matrix)

    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            temp = matrix[n - 1- j][i]
            matrix[n - 1 - j ][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = temp
    return matrix

def rotate_anticlockwise(matrix):
    n = len(matrix)
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][n - 1 - i]
            # 0, 0 = 0, 2
            # 1, 0 = 1, 2
            matrix[j][n - 1 - i] = matrix[n - 1 - i][n - 1 - j]
            #0, 2 = 2, 2
            # 1, 2 = 2, 1
            matrix[n - 1- i][n - 1 - j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = temp

    return matrix


def rotate_180(matrix):
    n  = len(matrix)

    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            temp1 = matrix[i][j]
            matrix[i][j] = matrix[n  - 1 - i][n - 1 - j]
            matrix[n  - 1 - i][n - 1 - j] = temp1

            temp2 = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i]= matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp2
    return matrix


if __name__ == '__main__':
    print(rotate_clockwise(matrix1))
    print(rotate_anticlockwise(matrix1))

    for _ in range(2):
        rotate_clockwise(matrix1)
        print(rotate_180(matrix1))