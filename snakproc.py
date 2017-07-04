import re
R=int(input())
n=1
while n<=R:
	L=int(input())
	r=input()
	pattern=r"^((\.)*H(\.)*T(\.)*)+$"
	result=re.match(pattern,r)
	if result or re.match("^(\.)*$",r):
		print('Valid')
	else:
		print('Invalid')
	n+=1
