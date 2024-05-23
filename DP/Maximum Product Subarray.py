# Maximum Product Subarray
def maxProduct(nums):
    res = max(nums)
    curMin, curMax = 1, 1
    tmp = 0
    for n in nums:
        if n == 0:
            curMin, curMax = 1, 1
            continue
        tmp = n * curMax
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        res = max(res, curMax)
    return res

