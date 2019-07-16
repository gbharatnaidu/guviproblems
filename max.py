n=int(input())
lst=input()
lst=lst.split()
lst=list(map(int,lst))
for i in range(0,len(lst)):
  print(max(lst),end=" ")
  lst.remove(max(lst))
  print(min(lst),end=" ")
  lst.remove(min(lst)) 
