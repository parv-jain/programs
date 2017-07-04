T=int(input())
n=1
while n<=T:
	N=int(input())
	ans=0
	cap=1
	while N >= cap:
		N-=cap
		cap+=1
		ans+=1
	if N>=1:
		ans+=1
	print (ans)
	n+=1

