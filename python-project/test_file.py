def testReturnOr(string, num):
    return string == 'hello' or num < 4

if __name__ == '__main__':
    if  testReturnOr('hello', 5):
        print('True')
    else:
        print ('False')
    if  testReturnOr('a', 3):
        print('True')
    else:
        print ('False')
    if  testReturnOr('a', 6):
        print('True')
    else:
        print ('False')
    if  testReturnOr('hello', 0):
        print('True')
    else:
        print ('False')
