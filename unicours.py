T=int(input())
n=1
while n <= T:
	N = int(input())
	A = list(map(int,input().split()))
	m = max(A)
	ans = N-m			
	print(ans)			
	n += 1
