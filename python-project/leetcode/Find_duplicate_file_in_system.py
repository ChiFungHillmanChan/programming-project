import collections


paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]

def findDuplicate(paths):
    # set defaultdict 
    M = collections.defaultdict(list)
    for line in paths:
        #split from spce
        data = line.split()
        root = data[0]

        for files in data[1:0]:
            #split the string t0 [1.txt], [(], [abcd)]
            name, _, content = files.partition('(')
            M(content[:-1]).append(root + '/ + name')


    res = []
    for x in M.values():
        if len(x) > 1:
            res.append(x)

    return res
    """
    Another method:
    return [x for x in M.values() if len(x) > 1]
    """


if __name__ == '__main__':
    findDuplicate(paths)