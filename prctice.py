def sliding_window(arr, k):
    if len(arr) < k:
        return None
    max_sum = float("-inf")
    window_sum = sum(arr[:k])
    max_sum = max(max_sum, window_sum)
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

print(sliding_window([1,2,3,4,5,6], 2))
