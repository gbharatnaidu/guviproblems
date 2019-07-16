n=int(input())
lst=input()
emp=[]
lst=lst.split()
lst=list(map(int,lst))
for i in range(0,n):
 if lst.count(i)==1:
   print(lst[i])
