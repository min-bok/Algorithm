arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
    
    return arr

print(sort(arr)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
