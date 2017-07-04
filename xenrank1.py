T=int(input())
n=1
while n<=T:
	U,V=map(int,input().split())
	offset1=V-1
	fo1=(offset1*(offset1+1))//2
	offset2=U-1
	fo2=(offset2*(offset2+1))//2
	ans=((U+1)*(V+1))-1+fo1+fo2
	ans+=U	
	print(ans+1)	
	n+=1	
