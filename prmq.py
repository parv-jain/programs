N=int(input())
a=list(map(int,input().split()))

def isPrime(n):
	if n==2 or n==3: return True
	if n%2==0 or n<2: return False
	for i in range(3,int(n**0.5)+1,2):
		if n%i==0:
			return False    
 
	return True
def F(L,R,X,Y):
	result=0
	for i in range(X,Y+1):
		if isPrime(i):
			for j in range(L,R+1):
				number = a[j-1]
				exponent = 0
				while number % i == 0:
					exponent = exponent+1
					number = number//i
				result += exponent
	return result

Q=int(input())
for i in range(Q):
	L,R,X,Y=map(int,input().split())
	print(F(L,R,X,Y)) 
