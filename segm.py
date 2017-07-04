T=int(input())
n=1
while n<=T:
	S=input()
	flag=0
	f=0
	for i in range(len(S)):
		if S[i] == '1':
			f=1
			break
	if f==0:
		print ('NO')
	else:
		for i in range(len(S)):
			if S[i] == '1':
				for j in range(i+1,len(S)):
					if S[j] == '0':
						for k in range(j+1,len(S)):
							if S[k]=='1':
								flag=1
								break
					if flag==1:
						break
			if flag==1:
				break
		if flag==0:
			print('YES')
		else:
			print('NO')	
	n+=1
