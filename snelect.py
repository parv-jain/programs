T=int(input())
n=1
while n<=T:
	s=input()
	e={}
	for i in range(len(s)):
		e[i]=0
	m,sn,ct=0,0,0
	for i in range(len(s)):
		if s[i]=='m' and e[i]!=1 and len(s)>1:
			if i>0 and s[i-1]=='s':
				e[i]=1
			elif i<len(s) and s[i+1]=='s':
				e[i]=1
	for i in range(len(s)):
		if e[i]==1:
			ct+=1
					
	for i in range(len(s)):
		if s[i]=='m':
			m+=1
		else:
			sn+=1
	sn-=ct
	if m>sn:
		print('mongooses')
	elif sn>m:
		print('snakes')
	else:
		print('tie')
	n+=1
						
