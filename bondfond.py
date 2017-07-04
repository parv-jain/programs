import math
T=int(input())
n=1
while n <= T:	
	N=int(input())
	i=math.ceil(math.log(N,2))	
	if math.fabs(2**i-N) <= math.fabs(2**(i-1)-N):
		print(int(math.fabs(2**i-N)))
	else:
		print(int(math.fabs(2**(i-1)-N)))  
	n+=1
	
