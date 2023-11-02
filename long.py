def long(lis):
    maxl=len(list[0])
    temp=list[0]
    for i in lis:
        if(len(i)>maxl):
            maxl=len(i)
            temp=i
    print("the word with longrstlength is ",temp," and length is ",maxl)
lis=[]
n=int(input("enter the list size "))
for i in range(0,n):
    a=input("enter the word to insert ")
    lis.append(a)
print(lis)
long(lis)
