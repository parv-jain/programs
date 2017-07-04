T=int(input())
t=1
while t<=T:
	n=int(input())
	row1=input()
	row2=input()
	f=0
	d=0
	s=0
	ar=[0] * n
	for i in range(n-1):
		if row1[i]=='*' and row1[i+1]=='*':
			f+=1
			ar[i]=1
		elif row2[i]=='*' and row2[i+1]=='*':
			f+=1
			ar[i]=1
	for i in range(n):
		if row1[i]=='*' and row2[i]=='*':
			d+=1
		if i<n-1 and row1[i]=='*' and row2[i+1]=='*' and ar[i]!=1 :
			s+=1
			ar[i]=1
	for i in range(n-1):
		if row1[i]=='*':
			for j in range(i+2,n):
				if row1[j]=='*' and ar[j]!=1:
					f+=1
					ar[j]=1
			break
	for i in range(n-1):
		if row2[i]=='*':
			for j in range(i+2,n):
				if row2[j]=='*' and ar[j]!=1:
					f+=1
					ar[j]=1
			break
	if d>0:
		f+=1
	else:
		f+=s
	print(f)	
	t+=1
