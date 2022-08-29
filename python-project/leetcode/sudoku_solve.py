from re import L


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
TEST_TIME = 5

def print_board(board):
    print(board)
    return (board)

def solveSudoku(board, count):
    empty_space = [0, 0]

    if(not find_empty_space(board, empty_space)):
        return True

    row, col = empty_space[0], empty_space[1]
    print (">>>>>>>>>>>>>>>>>>>>>>>\n\n")
    for num in range(1, 10):
        num = str(num)
        if ( check_row_isSafe(board, row, num)) and check_col_isSafe(board, col, num) and check_box_isSafe(board, row - row%3, col - col%3, num):
            board[row][col] = str(num)
            for i in range(len(board)):
                print(board[i])
            if count == TEST_TIME:
                break
            else:
                count += 1
            if (solveSudoku(board, count)):
                return True
            else:
                board[row][col] = "."

    return False
def find_empty_space(board, empty_space_location):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if (board[row][col] == "."):
                empty_space_location[0] = row
                empty_space_location[1] = col
                return True
    return False


def check_row_isSafe(board, row, num):
    for i in range(len(board)):
        if board[row][i] == num:
            return False
    return True

def check_col_isSafe(board, col, num):
    for i in range(len(board[0])):
        if board[i][col] == num:
            return False
    return True

def check_box_isSafe(board, row, col, num):
    for i in range(3):
        for j in range(3):
            if board[i + row][j + col] == num:
                return False
    return True


def unit_test(res):
    ans = [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]
]

    if ans == res:
        print('Correct')
        return True
    else:
        print('Incorrect')
        for i in range(len(res)):
            for j in range(len(res[0])):
                if res[i][j] != ans[i][j]:
                    print('Incorrect place[%i][%i] Your answer is:%i, The correct one is:%i', i, j, res[i][j], ans[i][j])
    return False
if __name__ == '__main__':
    solveSudoku(board, 0)
    # unit_test(board)
    # print_board(board)

