def print_formatted(number):
    nums = []
    for i in range(1, number+1):
        d = str(i)
        o = str(oct(i)[2:])
        h = str(hex(i)[2:]).upper()
        b = str(bin(i)[2:])
        nums.append([d, o, h, b])
        
    mw = len(nums[-1][3])
    for i in nums:
        print(*(rep.rjust(mw) for rep in i))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
