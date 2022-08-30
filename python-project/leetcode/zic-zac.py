def main(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    L = [''] * numRows
    index, step = 0, 1

    for i in s:
        L[index] += i
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step
        print(index, L)
    return ''.join(L)

def test(s, rows):
    test = main(s, rows)
    solution = 'PAHNAPLSIIGYIR'
    print(test, rows)
    if test == solution:
        print('True')
    else:
        print('False')

if __name__ == '__main__':
    test("PAYPALISHIRING", 3)
