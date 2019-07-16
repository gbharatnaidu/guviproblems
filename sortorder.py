n=int(input())
lst=input()
k=0
emp=[]
lst=lst.split()
lst=list(map(int,lst))
for i in range(0,n):
 if lst[i]==i:
   emp.append(i)
   k=1
for i in range(0,len(emp)):
  print(min(emp),end=" ")
  emp.remove(min(emp))
  if(k==0):
    print("-1")
