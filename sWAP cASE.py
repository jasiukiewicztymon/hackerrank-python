def swap_case(s):
    res = ""
    for _ in s:
        if _.isupper():
            res += _.lower()
        else:
            res += _.upper()
    return res

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
