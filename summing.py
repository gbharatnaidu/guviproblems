n=int(input())
lst=input()
lst=lst.split()
lst=list(map(int,lst))
for i in range(0,n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      if((lst[i]+lst[j])==lst[k]):
        print(lst[i]," ",lst[j]," ",lst[k])
