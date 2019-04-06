#include<stdio.h>
#include<math.h>
int T,n=1;
long long int N,temp,r,pr;	
int main(){
	scanf("%d",&T);
	while (n<=T){
		scanf("%lld",&N);
		while (N>=0){
			temp=N;
			r=temp%10;
			temp = exp(log(temp)-log(10));
			A:
			if (temp>32768){
			pr=r;
			r=temp%10;
			temp=exp(log(temp)-log(10));
			if(pr<r) goto B;
			goto A;	
			}
			while (temp>0){
				pr=r;
				r=temp%10;
				if(pr<r)  break;
				temp=temp/10;				
			}
			B:
			if(temp == 0)  break;
			N-=1;
		}
		printf("Case #%d: %lld\n",n,N);
		n+=1;	
	}	
	return 0;
}

