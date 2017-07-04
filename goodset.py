T=int(input())
n=1
while n<=T:
	x=int(input())
	L=[]
	count=1	
	while len(L)!=x:
		flag=0
		i=0
		while i<len(L):
			j=0
			while j<len(L):
				if j!=i and L[i]+L[j] == count:
					flag=1
					break
				j+=1
			if flag==1:
				break
			i+=1
		if flag==0:
			L.append(count)
		count+=1
	for a in L:
		print(a,end=' ')
	print()
	n+=1

