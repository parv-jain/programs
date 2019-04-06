#include<iostream>
using namespace std;
int main(){
	int i,j,n,f,dif,s,row,col,count;
	f=1;
	dif=22;
	s=6;
	cin>>n;
	f=n*(n+1)/2;
	row=1;
	col=0;
	count=1;
	for(j=1;j<=n-count;j++)
		cout<<" ";
	for(i=1;i<=f;i++){		
		if(s<10)		
		cout<<"0000"<<s<<" ";		
		else if(s<100)		
		cout<<"000"<<s<<" ";		
		else if(s<1000)		
		cout<<"00"<<s<<" ";		
		else if(s<10000)		
		cout<<"0"<<s<<" ";		
		else
		cout<<s<<" ";		
		
		s+=dif;
		dif+=16;
		col++;
		
		if (col==count){
			cout<<endl;
			col=0;
			count+=1;
			for(j=1;j<=n-count;j++)
				cout<<" ";
	
		}	
	}	
	return 0;
}
