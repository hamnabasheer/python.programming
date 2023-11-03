import math
n=int(input(" \n enter the limit \n"))
lst=[]
for i in range(999,n):
    z=math.sqrt(i)
    if z.is_integer():
        list.append(str(i))
print(list)
elist=[]
for i in lst:
    count=0
    for z in i:
        if int(z)%2==0:
            count=count+1
        else:
            break
    if count==4:
        elist.append(int(i))
print(elist)
    
