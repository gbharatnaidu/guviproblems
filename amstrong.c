#include<stdio.h>
int main(){
int n,c=0,sum=0,rem;
scanf("%d",&n);
int k=n,m=n;
while(n>0){
    c++;
    n=n/10;
}
while(k>0){
    rem=k%10;
    sum=sum+pow(rem,c);
    k=k/10;
}
if(sum==m)
    printf("yes");
else
    printf("no");
return 0;
}
