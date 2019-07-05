#include<stdio.h>
#include<string.h>
int main(){
char s1[100],s2[100];
int i;
scanf("%s%s",s1,s2);
int l=strlen(s1);
for(i=0;s2[i]!='\0';i++){
    s1[l]=s2[i];
    l++;
}
s1[l]='\0';
printf("%s",s1);
return 0;
}
