arr = []
for _ in range(int(input())):
    line = input().split(' ')
    arr.append(line)
    
name = input()

for _ in arr:
    if _[0] == name:
        print("{0:.2f}".format((float(_[1]) + float(_[2]) + float(_[3])) / 3))
