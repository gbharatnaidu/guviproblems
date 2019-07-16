n=int(input())
lst=input()
emp=[]
lst=lst.split()
lst=list(map(int,lst))
for i in range(0,n):
 if lst[i]==i:
   emp.append(i)
for i in range(0,len(emp)):
  print(min(emp),end=" ")
  emp.remove(min(emp))
