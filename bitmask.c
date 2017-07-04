#include<stdio.h>
int i,j,k,m,T,N,M,L[100][100],ans=0;
int min(int ar[], int M){
	m=32768;
	for(k=0;k<M;k++){
		if(ar[k]<m)
			m=ar[k];
	}
	return m;
}
int main(){
	scanf("%d",&T);
	while(T--){
		ans = 0;
		scanf("%d",&N);
		scanf("%d",&M);
		for (i=0;i<N;i++){
			for(j=0;j<M;j++){
				scanf("%d",&L[i][j]);
			}
			ans+=min(L[i],M);
		}
		printf("%d\n",ans);
	}
	return 0;
}
