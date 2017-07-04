def ncsub(seq, s=0):
    if seq:
        x = seq[:1]
        xs = seq[1:]
        p2 = s % 2
        p1 = not p2
        return [x + ys for ys in ncsub(xs, s + p1)] + ncsub(xs, s + p2)
    else:
        return [[]] if s >= 3 else [] 
N,K=map(int,input().split())
A=list(map(int,input().split()))
sub=[]	
c=0
L=ncsub(A,N)
for e in L:
	p=1
	for a in e:
		p=p*a
	if p<K and e:
		c+=1
print(c)

