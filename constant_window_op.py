arr=list(map(int,input().split())) #T.C=O(N)
k=int(input())
n=len(arr)
left=0
right=k-1
sum=sum(arr[left:right+1])
maxsum=sum
while(right<n-1):
    sum-=arr[left]
    left+=1
    right+=1
    sum+=arr[right]
    maxsum=max(maxsum,sum)
print(maxsum)    
