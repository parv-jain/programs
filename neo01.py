T=int(input())
n=1
while n<=T:
	N=int(input())
	A=list(map(int,input().split()))
	neg=list(filter(lambda x:x<0,A))
	pos=list(filter(lambda x:x>=0,A))
	ans,f,k=0,0,0
	for a in neg:
		ans+=a
	for a in pos:
		f+=a
	k=f*len(pos)	
	nans=ans	
	s=ans
	ans+=k	
	if set(A)!=set(neg):
		neg.sort(reverse=True)
		c=1
		for m in neg:
			f=f+m
			k=f*(len(pos)+c)
			c+=1
			nans=nans-m+k
			if nans>ans:
				ans=nans
				nans=s-m
				s=nans
			else:
				break				
	print(ans)	
	n+=1 
 
