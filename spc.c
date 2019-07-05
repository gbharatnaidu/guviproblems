#include<stdio.h>
int main(){
char str[100];
int count=0,i;
gets(str);
for(i=0;str[i]!='\0';i++){
    if(!((str[i]>=97 && str[i]<=122) || (str[i]>=0 && str[i]<=9)))
        count++;
}
printf("%d",count);
return 0;
}
