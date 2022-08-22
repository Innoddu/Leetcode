def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = (len(nums))
        for i in range(length):
            for j in range(length):
                if i == j:
                    j+=1
                val = nums[i] + nums[j]
                if val == target:
                    new_lst = [i,j]
                    return new_lst

def isPalindrome(x):
    """
        :type x: int
        :rtype: bool
    """
    if x < 0:
        return False
    temp = x
    reverse = 0
    while x:
        last = x % 10
        reverse = reverse * 10 + last
        x = x // 10
    return reverse == temp









  

        



    
    


        