def aggressiveCows(stalls, k):
    def canWePlace(minDist, stalls, k):
        cow = stalls[0]
        placedCows = 1
        for stall in range(1, len(stalls)):
            if (stalls[stall] - cow >= minDist):
                cow = stalls[stall]
                placedCows += 1
                if (placedCows >= k):
                    return True
        if (placedCows < k):
            return False

    # write code here
    stalls.sort()
    Min = min(stalls)
    Max = max(stalls)
    if (k == 2):
        return Max - Min
    low=1
    high=max(stalls)
    while(low<=high):
        minDist=(low+high)//2
        if(canWePlace(minDist,stalls,k)):
           low=minDist+1
        else:
            high=minDist-1
    return high        

# ✅ Driver Code
if __name__ == "__main__":
    stalls = [1, 2, 4, 8, 9]
    k = 3
    result = aggressiveCows(stalls, k)
    print("Largest minimum distance:", result)
