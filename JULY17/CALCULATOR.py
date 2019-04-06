T=int(input())
n=1
while n<=T:
	N,B=map(int,input().split())
	ssL=[]
	for fs in range(N):
		m=(N-fs)//B		
		ssL.append(m*fs)
	print(max(ssL))
	n+=1
