from itertools import permutations

def main(n):
    for array in permutations(str(n)):
        binary_number = bin(int("".join(array)))
        if binary_number.count('1') == 1 and array[0] != '0':
            return True
    return False

def faster_solution(n):
    return any( array[0] != '0' and bin(int("".join(array))).count('1') == 1 for array in permutations(str(n)))
if __name__ == '__main__':
    n = [10, 1, 128]
    for i in n:
        main(i)
        
    for i in n:

        if (faster_solution(i)):
            print('True')
        else:
            print('False')
    