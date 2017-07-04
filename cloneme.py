T=int(input())
n=1
while n<=T:
	N,Q=map(int,input().split())
	A=list(map(int,input().split()))
	for i in range(Q):
		a,b,c,d=map(int,input().split())
		sub1=A[a-1:b]
		sub2=A[c-1:d]
		sub1.sort()
		sub2.sort()
		c=0
		for i in range(len(sub1)):
			if sub1[i]!=sub2[i]:
				c+=1
				if c>1:
					break
		if c>1:
			print("NO")
		else:
			print("YES")
	n+=1
