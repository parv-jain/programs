# cook your dish here
T=int(input())
t=1
while t<=T:
    n=int(input())
    h=list(map(int,input().split()))
    ctr=1
    op=0
    for i in range(n):
        if h[i]==ctr:
            ctr+=1
        elif h[i]>ctr:
            d=h[i]-ctr
            h[i]-=d
            op+=d
            ctr+=1
        else:
            if i<n/2:
                d=h[i]-0
                op+=d
                h[i-1]=0
            continue
    nctr=max(h)-1
    k=int(n/2)+1
    for i in range(k,n):
        if h[i]==nctr:
            nctr-=1
        elif h[i]>nctr:
            d=h[i]-nctr
            h[i]-=d
            op+=d
            nctr-=1
        else:
            d=h[i]-0
            op+=d
            h[i]=0
    print(op)
    print(h)
    t+=1



