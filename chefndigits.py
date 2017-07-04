T=int(eval(input()))
n=1
while n<=T:
	L,R=map(int,input().split())
	A=list(map(int,input().split()))
	like=0
	if all([ v == 0 for v in A ]) :
		if R > 1023456788:
			for num in range(102345688,R+1):
				flag=0
				for i in range(10):
					count=0
					temp=num
					while temp > 1023456788:
						r=temp%10
						temp=temp//10
						if r == i:
							count+=1
					if count == A[i]:
						flag=1
						break
				if flag == 0:
					like+=1						
		print(like)
	else:	
		for num in range(L,R+1):
			flag=0
			for i in range(10):
				count=0
				temp=num
				while temp > 0:
					r=temp%10
					temp=temp//10
					if r == i:
						count+=1
				if count == A[i]:
					flag=1
					break
			if flag == 0:
				like+=1
		print (like)
	n+=1
