from math import pow
T=int(input())
n=1
while n<=T:
	p,q,r=map(int,input().split())
	A=[int(x) for x in input().split()]
	B=[int(x) for x in input().split()]
	C=[int(x) for x in input().split()]
	ans=0
	A.sort()
	B.sort()
	C.sort()
	f=lambda x,y,z : x*y + pow(y,2) + x*z + y*z		
	for c in C:
		nB=filter(lambda b:b>=c,B)
		for nb in nB:	
			nA=filter(lambda a: a<=nb, A)
			for na in nA:
				x=f(na,nb,c) 
				ans+=x
	ans=int(ans)
	print(ans%1000000007)
	n+=1
