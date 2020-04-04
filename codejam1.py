import numpy as np

t = int(input())

for i in range(t):
    n = int(input())

    cold = [[] * 3] * 3
    cold = np.zeros((n, n))

    countR = 0
    countC = 0

    for j in range(n):
        s = input().split(" ")
        rowd = []
        for k in s:
            if k in rowd:
                countR += 1
                break
            rowd.append(k)
        
        for k in range(len(s)):
            cold[k][j] = s[k]
    
    for j in cold:
        rowd = []
        for k in j:
            if k in rowd:
                countC += 1
                break
            rowd.append(k)

    print("Case #" + str(i + 1) + ":", int(cold.trace()) ,countR, countC)