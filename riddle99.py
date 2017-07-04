T=int(input())
n=1
while n<=T:
	A,B,M=map(int,input().split())
	count=0
	x=A
	j=x//M
	f=0
	if x%M!=0:
		while x%M!=0 or x<=A:
			x=M*j
			j+=1
			if x>B:
				f=1
				break
	if f==0:
		count+=1	
		off=B-x
		count = count + off//M
	n+=1
	print(count)
