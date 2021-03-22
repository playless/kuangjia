list=[1,3,5,7,0,3,4,0,9,8]
n=len(list)
print(n)
for j in range(1,n):
    for i in range(0,n-1):
        if list[i]>list[i+1]:
            list[i],list[i+1]=list[i+1],list[i]
    print(list)
print(list)