T=int(input())
n=1
while n<=T:
	U,V=map(int,input().split())
	Lx=[]
	Ly=[]
	C={}
	for i in range(U+V+1):
		Lx.append(i)
	for i in range(U+V+1):
		Ly.append(i)
	cno=1
	for x in Lx:
		for y in Ly:
			if (x+y) <= (U+V):
				C[cno]=[x,y]
				cno+=1
	ans=0
	for key in C:
		L=C[key]
		if sum(L)<(U+V):
			ans+=1
	
	x=0	
	y=U+V
	while x!=U and y!=V:
		ans+=1
		x+=1
		y-=1		
	print(ans+1)
	n+=1	
