import numpy as np

arr1, arr2 = [], []

n, m, p = list(map(int, input().split()))
for i in range(n):
    arr1.append(list(map(int, input().split())))
for i in range(m):
    arr2.append(list(map(int, input().split())))
    
narr1 = np.array(arr1)
narr2 = np.array(arr2)

print(np.concatenate((narr1, narr2), axis=0))
