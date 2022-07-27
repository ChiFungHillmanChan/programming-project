
def main(s):
    a = [str(i) for i in s]
    sign = ['.','+', '-']
    checklist = []
    result = 0
    for i in a:
        if not ' ':
            if not i.isdigit():
                break
        elif i.isdigit() or i in sign:
            checklist.append(i)
    if not checklist:
        return result
    result = int("".join(checklist))
    if result > 2**31 - 1:
        result = 2**31 - 1
    elif result < -2**31:
        result = -2**31
    return result
if __name__ == '__main__':
    print(main("words and 987"))