T = int(input())
n = 1
while n <= T:
	N,K=map(int,input().split())
	S = input()
	L = []
	for i in range(N-1):
		if S[i] == 'a':
			c=0
			for j in range(i+1,N):
				if S[j] == 'b':
					c+=1
			L.append(c)
	sum = 0	
	for i in range(0,len(L)):		
		sum = sum + (L[i]*(K-i))
	sum = sum + sum*(K-i)
	print(sum)
	n+=1	
