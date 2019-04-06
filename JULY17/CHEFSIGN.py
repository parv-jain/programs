T=int(input())
n=1
while n<=T:
	S=input()
	NS=''
	x=0
	m=0
	if S[0]=='>':		
		x=2
		m=2	
	else:
		x=1
		m=1
	NS+=str(x)
	k=1
	for s in S:
		if s=='=':
			NS+=s
			NS+=str(x)
			k+=2
		elif s=='<':
			x+=1
			NS+=s
			NS+=str(x)
			k+=2
		else:
			if x>=2:
				x-=1		
			else:
				NS=NS[:k]
				NS+='2'
				x=1				
			NS+=s	
			NS+=str(x)		
		if x > m:
			m=x
	print(NS)
	print(m)
	n+=1
