#include<stdio.h>
int main(){
int n,a=1,b=1,c,i;
scanf("%d",&n);
printf("%d %d ",a,b);
for(i=1;i<=n-2;i++){
    c=a+b;
    a=b;
    b=c;
    printf("%d ",c);
}
return 0;
}
