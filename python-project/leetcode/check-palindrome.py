def main(words):
    #check if words is alpha and transform to lower case
    answer = "".join(x for x in words if x.isalpha()).lower()

    # [::-1] is to change the order of the words
    # list[<start index> : <stop index> : <step>]
    if answer == answer[::-1]:
        print("True")
        return True
    else:
        print("False")
        return False

if __name__ == '__main__':
    main("A man, a plan, a canal: Panama")

