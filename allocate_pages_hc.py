def canweallocate(maxpages, arr, m):
    no_of_pages_allocated = arr[0]
    student = 1
    for pages in range(1, len(arr)):
        if (arr[pages] + no_of_pages_allocated <= maxpages):
            no_of_pages_allocated += arr[pages]
        else:
            no_of_pages_allocated = arr[pages]
            student += 1
    return student

def find_minimum_maxpages(arr, m):
    if m > len(arr):
        return -1
    min_pages = max(arr)
    max_pages = sum(arr)
    for maxpages in range(min_pages, max_pages + 1):
        if (canweallocate(maxpages, arr, m) <= m):
            return maxpages
    return -1

# Driver code
if __name__ == "__main__":
    arr = [12, 34, 67, 90]  # example array
    students = 2              # number of students
    result = find_minimum_maxpages(arr, students)
    print("Minimum of the maximum number of pages:", result)
