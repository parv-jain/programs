T=int(input())
n=1
while n<=T:
	name=input()
	formatted_name=''
	parts=name.split()
	count=0
	for part in parts:
		parts[count]=part.capitalize()
		count+=1
	for i in range(count-1):
		formatted_name+=parts[i][0]
		formatted_name+='. '
	formatted_name+=parts[count-1]
	print(formatted_name)
	n+=1
	
