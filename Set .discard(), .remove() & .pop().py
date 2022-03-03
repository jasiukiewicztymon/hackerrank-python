n = int(input())
s = set(map(int, input().split()))

n = int(input())
for _ in range(n):
    name = input().split(' ')
    if name[0] == "pop":
        s.pop()
    elif name[0] == "remove":
        s.remove(int(name[1]))
    else:
        s.discard(int(name[1]))
        
print(sum(s))
