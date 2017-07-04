T=int(input())
n=1
while n<=T:
	p,q,r=map(int,input().split())
	A=[int(x) for x in input().split()]
	B=[int(x) for x in input().split()]
	C=[int(x) for x in input().split()]
	ans=0
	A1=[]
	C1=[]
	m=[[0,0] for i in range (100001)]	
	A.sort()
	B.sort()
	C.sort()	
	
	def binary1(num,h):
		l=0
		if A[0]>num:
			return -1
		elif A[h]<=num:
			return h
		else:
			while l!=h-1:
				mid=(l+h)//2
				if A[mid]<=num:
					l=mid
				elif A[mid]>num:
					h=mid
			return l			
	def binary2(num,h):
		l=0
		if C[0]>num:
			return -1
		elif C[h]<=num:
			return h
		else:
			while l!=h-1:
				mid=(l+h)//2
				if C[mid]<=num:
					l=mid
				elif C[mid]>num:
					h=mid
			return l
	s=0
	for i in range (len(A)):
		s+=A[i]		
		A1.append(s)
	s=0
	for i in range (len(C)):
		s+=C[i]		
		C1.append(s)
	
	for i in range(q):
		m[i][0]=binary1(B[i],p-1);
		m[i][1]=binary2(B[i],r-1);
		print(m[i][0],m[i][1])
		if m[i][0]!=-1 and m[i][1]!=-1:
			s=m[i][0]
			u=m[i][1]
			ans=ans+(B[i]*(u+1)*A1[s])+(A1[s]*C1[u])+((u+1)*(s+1)*B[i]*B[i])+(B[i]*(s+1)*C1[u]);
	ans=int(ans)
	print (ans%1000000007)
	n+=1
