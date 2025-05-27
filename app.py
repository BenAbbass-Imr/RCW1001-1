

mylist = [1,2,5,10,8]

i,j=0,len(mylist)-1

while(i<j):
    temp=mylist[i]
    mylist[i]=mylist[j]
    mylist[j]=temp
    i+=1
    j-=1

print(f"final list:{mylist}")