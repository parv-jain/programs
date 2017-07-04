import itertools
T=int(input())
n=1
while n <= T:
	N = int(input())
	A = list(map(int,input().split()))
	newA=[]	
	finA=[]
	m=0
	for newA in (list(itertools.permutations(A))): 
		B=[]
		newA=list(newA)
		for i in range(0,len(newA),2):
			if newA[i] > newA[i+1]:
				B.append(newA[i])
			else:
				B.append(newA[i+1])
		B.sort()		
		k=(len(B)+1)//2
		if B[k-1] > m:
			m=B[k-1]
			finA=newA
						
	print(m)
	ans = ''
	for e in finA:
		ans=ans+str(e)+' '
	print(ans)

	n += 1
