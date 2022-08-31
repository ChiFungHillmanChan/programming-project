def main(llist, n):

    sum = 0
    for i in llist:
        sum += i
    
    return ( int((n + 1)*n/2 - sum) )

if __name__ == '__main__':
    print(main( [1,3,5,6,2], 6 ))
    print(main( [1,2,3,4,5,7,8,9], 9))