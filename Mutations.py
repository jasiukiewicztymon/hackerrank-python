def mutate_string(string, position, character):
    out = ""
    for _ in range(len(string)):
        if _ == position:
            out += character
        else:
            out += string[_]
    return out

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new
