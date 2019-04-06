T = int(input())
n = 1
while n<T:
	st = list(map(str, input().split()))
	pc = st[0]
	k = int(st[1])
	for i in range(0,len(pc),3):
		if pc[i] == pc[i+1] and pc[i+1] == pc[i+2]:
			if pc[i] == '-':		
				pc[i] = '+'
				pc[i+1] = '+'
				pc[i+2] = '+'
			else :
				pc[i] = '-'
				pc[i+1] = '-'
				pc[i+2] = '-'
			
	print ("Case #"+str(n))
	n+=1
	
