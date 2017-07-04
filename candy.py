T = int(input())
n = 1
while n <= T:
	A,B = map(int,input().split())
	eat = 1	
	eata=0
	eatb=0
	player = 1
	
	while True:
		if player == 1:
			if eata <= A:
				eata += eat
				eat += 1
				player = 2
			else :
				break
		elif player == 2:
			if eatb <= B:
				eatb += eat
				eat += 1
				player =1
			else:
				break
	if player == 1:
		print ('Bob')
	elif player == 2:
		print ('Limak')
	n += 1
	
