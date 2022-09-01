candidates = [2, 3, 5, 7]
target = 7


def combinationSum(candidates, target):
    res = []

    #run dfs
    dfs(target, [], 0, res, candidates)
    print(res)
    return res

def dfs(target, temp, index, res, candidates):
    # can return
    if target == 0:
        return True
    # not allowed to be negative number
    elif target < 0:
        return False
    
    start = index


    while start < len(candidates):
        current = candidates[start]
        print(temp + [current])
        if dfs(target - current, temp + [current], start, res, candidates):
            res.append(list(temp) + [current])
        start += 1

if __name__ == '__main__':
    combinationSum(candidates, target)