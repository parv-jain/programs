def solve (a, b, n):
    # Write your code here
    k = min(a,b)
    i = 0
    x = min(a,b)
    while True:
        if k%a==0 or k%b==0:
            i+=1
        if i == n:
            break
        k+=1
    return k
T = int(input())
for _ in range(T):
    a,b,n = map(int,input().split())
    
    out_ = solve(a, b, n)
    print (out_)
