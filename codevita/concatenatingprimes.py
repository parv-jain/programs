def combinantorial(lst):
    pairs = []
    for element1 in lst:
        for element2 in lst:
            pairs.append((element1, element2))
    return pairs

def check(x):
	'''if x%2==0 or x%3==0 or x%4==0 or x%5==0 or x%6==0 or x%7==0 or x%8==0 or x%9==0:
		return False
	else:'''
	f=0
	for i in range(3,x//2+1):
		if x%i==0:
			f=1
			break
	if f==1:
		return False
	else: 
		return True


N=int(input())
s=2
primes=[]
while s<=N:
	f=0
	for i in range(2,s//2+1):
		if s%i==0:
			f=1			
			break
	if f==0:
		primes.append(s)
	s+=1
#print(primes)
pairs=combinantorial(primes)
#print(pairs)
pairs=list(set(pairs))
ans=0
print(pairs)
for pair in pairs:
	num=str(pair[0])+str(pair[1])
	num=int(num)
	#print(num)	
	if check(num):
		print(num,end=' ')
		ans+=1
print()
print(ans)
