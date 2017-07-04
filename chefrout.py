import re
T=int(input())
n=1
while n<=T:
	S=input()
	f=0
	pattern1=r"^(C)+(E)*(S)*$"
	pattern2=r"^(E)+(S)*$"
	pattern3=r"^(S)+$"
	result1=re.match(pattern1,S)
	result2=re.match(pattern2,S)	
	result3=re.match(pattern3,S)	
	if (result1 or result2 or result3):
		print ('yes')
	else:
		print ('no')
	n+=1
