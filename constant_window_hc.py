arr=list(map(int,input().split())) #T.C=O(N POWER 2)
k=int(input())
n=len(arr)
summax=0
for i in range(0,n):
    for j in range(i,n):
        if(len(arr[i:j+1])==k):
            maxsum=max(summax,max(arr[i:j+1]))
print(maxsum)            
            
