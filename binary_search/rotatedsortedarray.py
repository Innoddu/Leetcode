def search(nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif target <= nums[m]:
                if target == nums[l]:
                    return l
                l = m + 1
            else:
                if target == nums[r]:
                    return r
                r = m - 1
        return -1
