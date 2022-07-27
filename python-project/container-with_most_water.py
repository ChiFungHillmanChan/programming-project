def main(height):
    maxnum = 0
    for i in range(len(height)):
        for j in range(len(height)):
            maxnum = max(maxnum, height[i] * (j))

    print(maxnum)
if __name__ == '__main__':
    main([1,8,6,2,5,4,8,3,7])