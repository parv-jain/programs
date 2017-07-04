T=int(input())
n=1
while n<=T:
	N=int(input())
	A=list(map(int,input().split()))
	B=list(map(int,input().split()))	
	L=[]
	ans=0
	for i in range(N):
		x=min(A)
		y=max(B)
		ans+=(x*y)
		A.remove(x)
		B.remove(y)	
	print (ans)
	n+=1

