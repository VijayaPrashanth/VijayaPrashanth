a=input("Please enter a string : ")
ls = []
def most_frequent(wor) :
  for i in wor :
    count=0
    for j in wor :
      if i==j :
        count=count+1
    ls.append(i)
    ls.append(count)
most_frequent(a)
dt = {ls[i] : ls[i+1] for i in range(0,len(ls),2)}
lt = list(dt.items())
l=len(lt)
for i in range(l-1):
  for j in range(i+1,1):
    if lt[i][1] < lt[j][1] :
      t = lt[i]
      lt[i] = lt[j]
      lt[j] = t
  sd = dict(lt)
for item in sd :
  print(item,":",sd[item])
