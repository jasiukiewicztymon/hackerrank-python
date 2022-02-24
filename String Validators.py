if __name__ == '__main__':
    s = raw_input()
    b = False
    for _ in s:
        if _.isalnum():
            b = True
            print(b)
            break
        
    if b == False:
        print(b)
    else:
        b = False
    
    for _ in s:
        if _.isalpha():
            b = True
            print(b)
            break
        
    if b == False:
        print(b)
    else:
        b = False
        
    for _ in s:
        if _.isdigit():
            b = True
            print(b)
            break
        
    if b == False:
        print(b)
    else:
        b = False
    
    for _ in s:
        if _.islower():
            b = True
            print(b)
            break
        
    if b == False:
        print(b)
    else:
        b = False
        
    for _ in s:
        if _.isupper():
            b = True
            print(b)
            break
        
    if b == False:
        print(b)
    else:
        b = False
