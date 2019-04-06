T = int(input())
Z = T+1
while T>0:
    N = int(input())
    t = N
    temp = 0
    A = 0
    B = 0
    z = ''
    flag = True
    while t > 0:
        r = t % 10
        t = t // 10
        temp = temp * 10 + r
        if flag and r == 0:
            z = z + str(r)
        else:
            flag = False
    while temp > 0:
        r = temp % 10
        temp = temp // 10
        if r == 4:
            A = (A*10) + 2
            B = (B*10) + 2
        else:
            if r == 8 or r == 9 or r == 7:
                x = 6
                y = r - x
            elif r % 2 == 0:
                x = r // 2
                y = x
            else:
                x = r // 2
                y = x + 1
            A = (A*10) + x
            B = (B*10) + y
    print("Case #{}: {} {}".format(Z-T, str(A)+z, str(B)+z))
    T-=1

