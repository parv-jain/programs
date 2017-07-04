#include<iostream>
using namespace std;
int T,i;
char s[100];
int ar[100];
int main(){
	cin>>T;
	while (T--){
		cin>>s;
		int l=0,ct=0,m=0,sn=0;
		for(i=0;s[i]!='\0';i++){
			ar[i]=0;
			l+=1;
	    	}
		for(i=0;s[i]!='\0';i++){
			if (s[i]=='m' && ar[i]!=1 && l>1){
				if (i>0 && s[i-1]=='s' && ar[i-1]==0)	{
				    ar[i-1]=-1;
				    ar[i]=1;	
				}
				else if(i<l && s[i+1]=='s' && ar[i+1]==0){
				    ar[i+1]=-1;
				    ar[i]=1;
				}
			}
		}
		for(i=0;s[i]!='\0';i++){
			if (ar[i]==-1)
				ct+=1;
		}
		for(i=0;s[i]!='\0';i++){
			if (s[i]=='m')
				m+=1;
			else
				sn+=1;
		}
		sn-=ct;
		
		if (m>sn)
			cout<<"mongooses\n";
		else if(sn>m)
			cout<<"snakes\n";
		else
			cout<<"tie\n";
	}
	return 0;
}
