t = int(input())

for r in range(t):
    s = list(input())
    temp = s

    res = ""
    arr = []
    avail = 0
    for i in temp:
        x = int(i)
        while avail > x:
            arr.append(")")
            avail -= 1
        if avail == 0:
            while x:
                arr.append("(")
                x -= 1
                avail += 1
        if avail < x:
            while x > avail:
                arr.append("(")
                avail += 1
        arr.append(i)
    while(avail):
        arr.append(")")
        avail -= 1
    print("Case #" + str(r + 1) + ":", ''.join(arr))