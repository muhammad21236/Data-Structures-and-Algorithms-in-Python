def BS(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return print(f"{target} found at index {mid}")
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    


arr = [1, 3, 5, 7, 9, 11, 15]


print(BS(arr, target=1))
