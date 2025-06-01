def findPages(arr, m):
    def canweallocate(maxpages, arr):
        no_of_pages_allocated = arr[0]
        student = 1
        for pages in range(1, len(arr)):
            if (arr[pages] + no_of_pages_allocated <= maxpages):
                no_of_pages_allocated += arr[pages]
            else:
                no_of_pages_allocated = arr[pages]
                student += 1
        return student

    if m > len(arr):
        return -1
    low = max(arr)
    high = sum(arr)
    while(low <= high):
        maxpages = (low + high) // 2
        if(canweallocate(maxpages, arr) <= m):
            high = maxpages - 1
        else:
            low = maxpages + 1
    return low

# ---------- User Input Handling ----------
# Input: space-separated integers for book pages
arr = list(map(int, input("Enter the number of pages in each book (space-separated): ").split()))
m = int(input("Enter the number of students: "))

# Call the function and print result
result = findPages(arr, m)
print("Minimum number of pages each student has to read:", result)
