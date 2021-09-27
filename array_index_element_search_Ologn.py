def find_index(arr, n, B):
 
    # Lower and upper bounds
    start = 0
    end = n - 1
 
    # Traverse the search space
    while start<= end:
 
        mid =(start + end)//2
 
        if arr[mid] == K:
            return mid
 
        elif arr[mid] < K:
            start = mid + 1
        else:
            end = mid-1
 
    # Return the insert position
    return end + 1
 
# Driver Code
arr = [1, 3, 5, 6]
n = len(arr)
K = 2
print(find_index(arr, n, K))
