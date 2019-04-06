
T = int(input())
n = 1
while n <= T:
	N=int(input())
	while N >= 0:
		temp = N
		r = temp%10
		while temp>0:
			pr = r
			r = temp%10	
			if pr < r:
				break
			temp= temp//10		
		if temp == 0:
			break
		N-=1	
	print ("Case #"+str(n)+": "+str(N))
	n+=1

