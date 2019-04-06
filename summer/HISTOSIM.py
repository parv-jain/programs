T=int(input())
n=1
while n<=T:
	P,Q=input().split()
	i=0	
	A=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	while i<len(P):		
		if P[i]!=Q[i]:
			if Q[i] not in P:
				P=P.replace(P[i],Q[i])
			
			'''else:
				for c in A:
					if c not in P:
						P=P.replace(P[i],Q[i])
				i-=1'''
		i+=1 
	print('{} {}'.format(P, Q))
	n+=1
