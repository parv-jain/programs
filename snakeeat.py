T=int(input())
n=1
while n<=T:
	N,Q=map(int,input().split())
	L=list(map(int,input().split()))
	max_len=max(L)
	for i in range(Q):
		K=list(map(int,input().split()))
		for k in K:
			if k<=max_len:
				short_than_k=list(filter(lambda x:x<k,L))
				l1=len(short_than_k)
				l=l1			
				while True:				
					m=max(short_than_k)
					mi=min(short_than_k)
					rem=k-m
					if rem<=(l-1):
						while rem!=0:
							mi=min(short_than_k)
							short_than_k.remove(mi)
							rem-=1
					else:
						break
					l=len(short_than_k)
				ans=N-l1
				if l < l1:
					ans+=l
			else:
				ans=0
			print(ans)
	n+=1
