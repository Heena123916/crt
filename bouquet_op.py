def minDaysBloom(m, k, arr):
        # Code here
        if(m>len(arr)):
            return -1 
        low=min(arr) 
        high=max(arr) 
        ans = -1 
        while(low<=high):
            bloomday=(low+high)//2 
            count=0 
            noOfB=0 
            for flower in arr:
                if(flower<=bloomday):
                    count+=1 
                else:
                    noOfB+=count//k 
                    count=0 
            noOfB+=count//k 
            if(noOfB<m):
                low=bloomday+1 
            else:
                ans=bloomday 
                high=bloomday-1 
        return ans
m=int(input())
k=int(input())
arr=list(map(int,input().split()))
print(minDaysBloom(m, k, arr))
    
