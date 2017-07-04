T = int(eval(input()))
n = 1
while n <= T:
	N,K = map(int,input().split());
	ING = [k for k in range(1,K+1,1)]
	flag = N
	for i in range(N):
		L = list(map(int,input().split()))
		L.pop(0)
		if flag == N:
			ING = list(filter(lambda x: x not in L, ING))
			if len(ING) == 0:
				flag = i
	if len(ING) == 0 and flag < N-1:
		print("some")
	elif len(ING) != 0:
		print("sad")
	else:
		print("all")			
	n += 1

    
