T=int(input())
n=1
while n<=T:
	N=int(input())
	L=[0,1,2,3,4,5,6,7,8,9]
	i=1
	temp=N
	if N==0:
		print("Case #"+str(n)+": INSOMNIA")
		n+=1
		continue
	while len(L)>0:	
		while temp>0:
			r=temp%10
			temp=temp//10
			try:
				L.remove(r)
			except ValueError:
				pass
		i+=1
		temp=N*i
	print ("Case #"+str(n)+": "+str(N*(i-1)))
	n+=1
	

