T=int(input())
n=1
while n<=T:
	x=0
	y=0
	M=int(input())
	steps=0
	seq=1
	fullseq=M//3
	rem=M%3
	x+=fullseq
	y+=fullseq
	y+=fullseq		
	steps=0
	while steps<rem:
		if seq==1:	
			x+=1
		else:
			y+=1
		seq+=1
		if seq>3:
			seq=1
		steps+=1
	print("{} {}".format(x, y))	
	n+=1	
