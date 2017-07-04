T=int(input())
n=1
while n<=T:
	N=int(input())
	b=[]
	cb=0
	for i in range(N):
		cb=float(input())
		b.append(cb)
	offset=79.6
	unsuccess=0
	start=0
	if cb<=79.6:
		if len(b)<=2:
			unsuccess = len(b)
		else:
			unsuccess = 2
	else:
		while offset <= cb+80:
			rl=2	
			for i in range(start,N):
				if b[i] <= offset and rl>0:
					unsuccess+=1
					rl-=1
				elif b[i] <= offset:
					continue
				else:
					start=i
					break
			offset+=80
	print(unsuccess)	
	n+=1
