t = int(input())
arr = []

for i in range(t):
    choice = input().split(' ')
    if choice[0] == 'insert':
        arr.insert(int(choice[1]), int(choice[2]))
    elif choice[0] == 'print':
        print(arr)
    elif choice[0] == 'remove':
        arr.remove(int(choice[1]))
    elif choice[0] == 'append':
        arr.append(int(choice[1]))
    elif choice[0] == 'sort':
        arr.sort()
    elif choice[0] == 'pop':
        arr.pop()
    else:
        arr.reverse()
