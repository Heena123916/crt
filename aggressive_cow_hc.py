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
    for minDist in range(1, Max - Min + 1):
        if (canWePlace(minDist, stalls, k)):
            continue
        else:
            return minDist - 1

# ✅ Driver code
if __name__ == "__main__":
    # Simulating input: "0 3 4 7 10 9" and "3"
    stalls = list(map(int, "0 3 4 7 10 9".split()))
    k = 3

    result = aggressiveCows(stalls, k)
    print("Largest minimum distance:", result)
