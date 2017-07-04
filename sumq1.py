import bisect 
T=int(input())
n=1	
while n<=T:
	p,q,r=map(int, input().split())
	A=list(map(int,input().split()))
	B=list(map(int,input().split()))
	C=list(map(int,input().split()))
	ans=0
	A1=[]
	C1=[]	
	s=0
	A.sort()
	B.sort()
	C.sort()	
	for i in range (p):
		s+=A[i]		
		A1.append(s)
	s=0
	for i in range (r):
		s+=C[i]		
		C1.append(s)
	for i in range(q):
		if A[0]>B[i]:
			x=-1
		elif A[p-1]<=B[i]:
			x=p-1
		else:
			x=bisect.bisect(A,B[i])-1	
			
		if C[0]>B[i]:
			y=-1
		elif C[r-1]<=B[i]:
			y=r-1
		else:
			y=bisect.bisect(C,B[i])-1
		#print(x,y)
		if x!=-1 and y!=-1:
			s=x
			u=y
			ans=ans+(B[i]*(u+1)*A1[s])+(A1[s]*C1[u])+((u+1)*(s+1)*B[i]*B[i])+(B[i]*(s+1)*C1[u]);
	#ans=int(ans)
	print(ans%1000000007)
	n+=1
