import itertools
T=int(input())
n=1
while n<=T:
	N,P = map(int,input().split())
	seq = list(map(int,input().split()))
	max=0
	d=[]
	for k in range(1,N+1):
		L=zip(*(seq[i:] for i in range(k)))			
		for m in L:
			s=0
			for e in m:
				s+=e
			s=s%P
			if s>max:	
				max=s
			d.append(s)
	c=0
	for i in d:
		if i==max:
			c+=1
	print(str(max)+" "+str(c))	
	n+=1
				
