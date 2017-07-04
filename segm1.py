import re
T=int(input())
n=1
while n<=T:
	S=input()
	f=0
	for i in range(len(S)):
		if S[i] == '1':
			f=1
			break
	if f==0:
		print ('NO')
	else:
		pattern=r"(0)*(1)+(0)+(1)+"
		result = re.match(pattern,S)
		if result:
			print ('NO')
		else:
			print ('YES')
	n+=1
