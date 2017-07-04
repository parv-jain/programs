import itertools
T=int(raw_input())
n=1
while n<=T:
	N,K=map(int,raw_input().split())
	ans=0
	S=[]
	for i in range(N):	
		L=[int(x) for x in raw_input().split()]
		del L[0]
		L=set(L)
		S.append(L)
	#req={i for i in range(1,K+1)}
	idx=range(len(S))
	un=lambda a,b: S[a].union(S[b])
	pairs = itertools.combinations(idx, 2)
	for p in pairs:
		
		uni=un(p[0],p[1])
		if len(uni)>=K:
			ans+=1
	print(ans)
	n+=1  
