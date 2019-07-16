n=int(input())
lst=input()
lst=lst.split()
lst=list(map(int,lst))
for i in range(0,n):
 if(lst.count(lst[i])==2):
   print(lst[i])
   break
