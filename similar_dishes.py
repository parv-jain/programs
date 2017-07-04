T = int(eval(input()))
ctr = 1
while ctr <= T:
    L1 = list(map(str, input().split()))
    L2 = list(map(str, input().split()))
    flag = 0
    for i1 in L1:
        for i2 in L2:
            if i1 == i2:
                flag += 1
    if flag >= 2:
        print("similar")
    else:
        print("dissimilar")
    ctr += 1
