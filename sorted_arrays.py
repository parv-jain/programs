def solve (A, N, K):
    # Write your code here
    A = list(A)
    r = 1
    n = N
    mapping = {}
    totalElements = 0
    while N>0:
        for e in A[0:N]:
            if e in mapping.keys():
                mapping[e] += (r*n)
            else:
                mapping[e] = (r*n)
            totalElements += (r*n)
        N=N//2
        r+=1
    
    if K > totalElements:
        return -1
    
    till = 0
    for key in sorted(mapping):
        till += mapping[key]
        if K <= till:
            return key
            
T = int(input())
for _ in range(T):
    N = int(input())
    A = map(int, input().split())
    K = int(input())

    out_ = solve(A, N, K)
    print (out_)
