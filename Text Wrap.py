import textwrap

def wrap(string, max_width):
    out = ""
    for _ in range(len(string)):
        out += string[_]
        if (_ - max_width + 1) % max_width == 0:
            out += "\n"
    return out

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
