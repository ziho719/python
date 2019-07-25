n = int(input())      
m = int(input())

strs=[]
ori=[]

for index in range(m):
    p=str(input())
    for si in range(len(strs)):
        if(strs[si].find(p)>0):
            print(ori[si])
            break            
    else:
        strs.append(p+p)
        ori.append(index+1)
        print(0)