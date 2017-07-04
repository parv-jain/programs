import collections
N,K,P=map(int,input().split())
A=list(map(int,input().split()))
R=input()
for r in R:
	if r=='!':
		d=collections.deque(A)
		d.rotate(1)
		A=list(d)
	elif r=='?':
		ans=[]
		if K<=len(A): 
			L=zip(*(A[i:] for i in range(K)))
		else:
			L=zip(*(A[i:] for i in range(len(A))))			
		for e in L:
			c=0
			for a in e:
				if a==1:
					c+=1
			ans.append(c)	
		if ans:		
			print(max(ans)) 	

