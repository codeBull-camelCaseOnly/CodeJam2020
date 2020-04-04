
def intersect(a, b):
    if a[0] > b[0] and a[0] < b[1]:
        return True
    if a[1] > b[0] and a[1] < b[1]:
        return True
    return False

def intersectR(a, b):
    return intersect(a, b) or intersect(b, a) or a[0] == b[0] or a[1] == b[1]

t = int(input())

for r in range(t):
    n = int(input())

    arr = []
    for i in range(n):
        s = input().split(" ")
        data = (int(s[0]), int(s[1]), i)
        arr.append(data)

    orig = arr
    # keys = sorted(range(len(arr)), key=lambda k: arr[k][0])
    arr.sort(key=lambda x: x[0])
    print("Case #" + str(r + 1) + ": ", end='')
   
    arrj = []
    arrc = []
    ca = ja = 0
    possible = True
    for i in range(len(arr)):
        if arr[i][0] >= ca:
            arrj.append(arr[i][2])
            ca = arr[i][1]
        else:
            if arr[i][0] >= ja:
                arrc.append(arr[i][2])
                ja = arr[i][1]
            else:
                possible = False
                break
    
    if not possible:
        print("IMPOSSIBLE")
    else:
        res = [0] * len(arr)
        for i in arrj:
            res[i] = "J"
        for i in arrc:
            res[i] = "C"
        print(''.join(res))
