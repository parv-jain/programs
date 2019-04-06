T=int(input())
n=1
while n<=T:
	U,V,X=map(int,input().split())
	rs=U+V
	n+=1
	print(X/rs)
