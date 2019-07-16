n=int(input())
lst=input()
k=0
lst=lst.split()
lst=list(map(int,lst))
for i in range(0,n):
 if(lst.count(lst[i])>=2):
   print(lst[i])
   k=1
   break
if(k==0):
 print("unique")
