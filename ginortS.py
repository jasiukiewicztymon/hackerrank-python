string = input()

output = ""
low, up, num = [], [], []

for i in string:
    if i.isnumeric():
        num.append(i)
    elif i.isupper():
        up.append(i)
    else:
        low.append(i)
        
for i in sorted(low):
    output += i
for i in sorted(up):
    output += i
for i in sorted(num):
    if int(i) % 2 == 1:
        output += i
for i in sorted(num):
    if int(i) % 2 == 0:
        output += i
    
print(output)
