T=int(input())
n=1
while n<=T:
	N,M = map(int, input().split())
	cost = 0
	for i in range (N):
		L=[int(x) for x in input().split()]
		cost += min(L)
	print (cost)
	n+=1

