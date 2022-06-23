def main(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    i = 0
    num = 0
    while i < len(s):
        # check if it is IV IX XL XC CD CM
        # s[i:i+2] means from s index i to index i+2 (not include i+2)
        if i+1 < len(s) and s[i:i+2] in roman:
            num += roman[s[i:i+2]]
            i+=2
        else:
            num+=roman[s[i]]
            i+=1
    return num