T = int(input())
n = 1
while n <= T:
	st=str(input())
	d={}	
	ones=1
	for i in range(len(st)):
		if st[i] == '1':
			d[i] = ones
			ones+=1
	i=0
	time = 0
	pos = len(st)
	for pos in sorted(d):
		if i == 0:
			ppos = pos
			i = 1
			continue
		if (ppos+1) != pos:
			time = time + d[ppos] * (pos - ppos - 1) + d[ppos] 
		ppos = pos
	if pos < len(st) - 1:
		time = time + d[pos] * (len(st) - pos -1) + d[pos]
	print(time)
	n += 1

    
